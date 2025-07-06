from sqlalchemy import TIMESTAMP,ForeignKey,func
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import MappedColumn,mapped_column,relationship
from app.model.base import Base
from app.util.id_generator import generate_ulid
from typing import Optional

class UserModel(Base):
    __tablename__ = "users"

    id:MappedColumn[str] = mapped_column(
        VARCHAR(26),
        primary_key=True,
        index=True,
        nullable=False,
        unique=True,
        default=generate_ulid
    )

    name:MappedColumn[str] = mapped_column(
        VARCHAR(30),
        nullable=False
    )
    email:MappedColumn[str] = mapped_column(
        nullable=False,
        unique=True
    )
    password : MappedColumn[Optional[str]] = mapped_column(
        nullable=True
    )
    salt:MappedColumn[str] = mapped_column(nullable=False)
    created_at:MappedColumn[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )
    personas = relationship("PresonaModel",back_populates="user",cascade="all,delete")