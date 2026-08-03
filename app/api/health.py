import socket
from urllib.parse import urlparse

import redis
from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from app.config import settings
from app.db.session import engine

router = APIRouter()


def check_postgres() -> bool:
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return True


def check_redis() -> bool:
    client = redis.Redis.from_url(settings.redis_url)
    client.ping()
    return True


def check_livekit() -> bool:
    parsed = urlparse(settings.livekit_url)
    host = parsed.hostname
    port = parsed.port or (443 if parsed.scheme == "https" else 80)
    if host is None:
        raise ValueError("Invalid LIVEKIT_URL")
    with socket.create_connection((host, port), timeout=2):
        return True


@router.get("/health")
def health_check() -> dict:
    checks = {
        "postgres": False,
        "redis": False,
        "livekit": False,
    }

    errors: dict[str, str] = {}

    try:
        checks["postgres"] = check_postgres()
    except Exception as exc:  # pragma: no cover
        errors["postgres"] = str(exc)

    try:
        checks["redis"] = check_redis()
    except Exception as exc:  # pragma: no cover
        errors["redis"] = str(exc)

    try:
        checks["livekit"] = check_livekit()
    except Exception as exc:  # pragma: no cover
        errors["livekit"] = str(exc)

    overall_ok = all(checks.values())
    response = {"status": "ok" if overall_ok else "degraded", "checks": checks}
    if errors:
        response["errors"] = errors

    if not overall_ok:
        raise HTTPException(status_code=503, detail=response)

    return response
