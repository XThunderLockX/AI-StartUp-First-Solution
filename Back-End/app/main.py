from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core.config import settings


def create_app() -> FastAPI:

    app = FastAPI(title="Local Services Platform API", version="1.0.0")

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get("/health", tags=["health"]) 
    def health() -> dict:
        return {"status": "ok"}

    @app.get("/", tags=["root"]) 
    def root() -> dict:
        return {"service": "Local Services Platform API", "version": "1.0.0"}

    return app


app = create_app()


