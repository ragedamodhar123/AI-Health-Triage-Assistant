from fastapi import APIRouter, Depends, Query

from app.api.dependencies import get_symptom_service
from app.schemas.symptom import (
    SymptomResponse,
)
from app.services.symptom_service import (
    SymptomService,
)

router = APIRouter(
    prefix="/symptoms",
    tags=["Symptoms"],
)


@router.get(
    "",
    response_model=list[SymptomResponse],
)
def get_all(
    service: SymptomService = Depends(
        get_symptom_service
    ),
):
    return service.get_all()


@router.get(
    "/search",
    response_model=list[SymptomResponse],
)
def search(
    q: str = Query(..., min_length=1),
    service: SymptomService = Depends(
        get_symptom_service
    ),
):
    return service.search(q)