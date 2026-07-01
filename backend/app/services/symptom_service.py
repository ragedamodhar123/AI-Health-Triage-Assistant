from sqlalchemy.orm import Session

from app.repositories.symptom_repository import (
    SymptomRepository,
)
from app.services.base_service import BaseService


class SymptomService(BaseService):

    def __init__(self, db: Session):
        super().__init__(SymptomRepository(db))

    def search(
        self,
        keyword: str,
    ):
        return self.repository.search(keyword)

    def get_all(self):
        return self.repository.get_all_active()