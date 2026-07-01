from sqlalchemy import Boolean, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base
from app.models.base_model import BaseModel


class Symptom(Base, BaseModel):
    __tablename__ = "symptoms"

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        index=True,
    )

    normalized_name: Mapped[str] = mapped_column(
        String(100),
        index=True,
    )

    category: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )