from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.symptom_master import Symptom
from app.repositories.base_repository import BaseRepository


class SymptomRepository(BaseRepository[Symptom]):

    def __init__(self, db: Session):
        super().__init__(Symptom, db)

    def search(
        self,
        keyword: str,
        limit: int = 20,
    ):
        return (
            self.db.query(Symptom)
            .filter(
                func.lower(Symptom.name).contains(
                    keyword.lower()
                )
            )
            .filter(Symptom.is_active.is_(True))
            .limit(limit)
            .all()
        )

    def get_all_active(self):
        return (
            self.db.query(Symptom)
            .filter(Symptom.is_active.is_(True))
            .all()
        )

    def get_by_normalized_name(
        self,
        normalized_name: str,
    ):
        return (
            self.db.query(Symptom)
            .filter(
                Symptom.normalized_name == normalized_name
            )
            .first()
        )