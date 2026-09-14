from fastapi import APIRouter

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.leads import router as leads_router


api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["System"]
)

api_router.include_router(
    leads_router,
    tags=["Leads"]
)
