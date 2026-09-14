from fastapi import FastAPI

from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered sales operations and lead automation platform."
)


@app.get("/")
def root():
    return {
        "message": f"{settings.app_name} API",
        "status": "running",
        "version": settings.app_version
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.app_env
    }