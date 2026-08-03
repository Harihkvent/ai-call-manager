# ai-call-manager

AI phone assistant & multi-tenant SaaS platform scaffold for self-hosted voice agents.

## Stack

- Backend: FastAPI (Python)
- Database: PostgreSQL + pgvector
- Cache/broker: Redis
- Realtime voice: self-hosted LiveKit (SIP + WebRTC)
- STT: faster-whisper (local, CPU-first)
- LLM: Ollama (local)
- TTS: pluggable provider interface (mock implementation)

## Quick start

1. Start services:

```bash
docker compose up --build
```

2. Run migrations (in a second shell):

```bash
docker compose exec backend alembic upgrade head
```

3. Verify health checks:

```bash
curl http://localhost:8000/health
```

Expected response is `{"status":"ok", ...}` when Postgres, Redis, and LiveKit are reachable.

## Environment variables

Copy `.env.example` to `.env` and adjust as needed.

Required variables:

- `APP_ENV`
- `DATABASE_URL`
- `REDIS_URL`
- `LIVEKIT_URL`
- `LIVEKIT_API_KEY`
- `LIVEKIT_API_SECRET`
- `OLLAMA_BASE_URL`
- `OLLAMA_MODEL`
- `WHISPER_MODEL`

## Notes

- Telephony integration is currently stubbed through `LiveKitSIPStubProvider`.
- Real PSTN/SIP trunk connectivity is intentionally not implemented in this initial scaffold.
