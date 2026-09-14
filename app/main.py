from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="AI-powered sales operations and lead automation platform."
)


@app.get("/", tags=["System"])
def root():
    return {
        "name": settings.app_name,
        "status": "running",
        "version": settings.app_version,
        "docs": "/docs"
    }


app.include_router(
    api_router,
    prefix="/api/v1"
)