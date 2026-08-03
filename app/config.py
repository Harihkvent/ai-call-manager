from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_env: str = "development"
    database_url: str = "postgresql+psycopg2://postgres@localhost:5432/aicall"
    redis_url: str = "redis://localhost:6379/0"
    livekit_url: str = "http://localhost:7880"
    livekit_api_key: str = "devkey"
    livekit_api_secret: str = "devsecret"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama3.1:8b"
    whisper_model: str = "small"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
