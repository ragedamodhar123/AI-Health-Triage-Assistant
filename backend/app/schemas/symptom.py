from pydantic import BaseModel, ConfigDict


class SymptomResponse(BaseModel):
    id: int
    name: str
    normalized_name: str

    model_config = ConfigDict(from_attributes=True)


class SymptomSearchResponse(BaseModel):
    symptoms: list[SymptomResponse]