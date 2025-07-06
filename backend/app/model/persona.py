from sqlalchemy import TIMESTAMP,Text,func,ForeignKey
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import MappedColumn,mapped_column,relationship
from app.model.base import Base
from app.util.id_generator import generate_ulid

class PersonaModel(Base):
    __tablename__="personas"

    id:MappedColumn[str]=mapped_column(
        VARCHAR(26),
        primary_key=True,
        index=True,
        unique=True,
        default=generate_ulid
    )
    user_id:MappedColumn[str] = mapped_column(
        VARCHAR(26),
        ForeignKey("users.id"),
        nullable=False
    )
    name:MappedColumn[str]=mapped_column(
    VARCHAR(100),
    nullable=False
    )
    persona_prompt:MappedColumn[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at:MappedColumn[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )

    chats = relationship("ChatModel",back_populates="persona",cascade="all,delete")
    user = relationship("UserModel",back_populates="personas")