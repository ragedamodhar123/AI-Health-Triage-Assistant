from fastapi import APIRouter

from app.api.routes import health
from app.api.routes.symptom import router as symptom_router


api_router = APIRouter()

api_router.include_router(symptom_router)
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"],
)
