from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=("Back-End/.env", ".env"), env_file_encoding="utf-8", case_sensitive=False)

    # App
    env: str = "dev"
    debug: bool = True
    project_name: str = "local-services-platform"
    backend_host: str = "0.0.0.0"
    backend_port: int = 8000

    # CORS
    # Accept comma-separated env var CORS_ALLOW_ORIGINS, fallback to sensible defaults
    cors_allow_origins_raw: str = "http://localhost:5173,http://127.0.0.1:5173"

    @property
    def cors_allow_origins(self) -> List[str]:
        return [o.strip() for o in self.cors_allow_origins_raw.split(",") if o.strip()]

    # Database
    database_url: str = "postgresql+psycopg://postgres:postgres@db:5432/local_services"


@lru_cache
def get_settings() -> Settings:
    return Settings()  # type: ignore[call-arg]


settings = get_settings()


