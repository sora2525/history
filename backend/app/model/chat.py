from sqlalchemy import TIMESTAMP,ForeignKey,Enum as SqlEnum,Text,func
from sqlalchemy.dialects.postgresql import VARCHAR
from sqlalchemy.orm import MappedColumn,mapped_column,relationship
from enum import Enum
from app.model.base import Base
from app.util.id_generator import generate_ulid

class MessageType(str,Enum):
    USER = "user"
    AI = "ai"

class ChatModel(Base):
    __tablename__ = "chats"

    id:MappedColumn[str] = mapped_column(
        VARCHAR(26),
        primary_key=True,
        index=True,
        unique=True,
        default=generate_ulid
    )

    persona_id: MappedColumn[str] = mapped_column(
        VARCHAR(26),
        ForeignKey("personas.id",ondelete="CASCADE"),
        nullable=False
    )

    message_type:MappedColumn[MessageType] = mapped_column(
        SqlEnum(MessageType),
        nullable=False
    )
    message_text: MappedColumn[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at:MappedColumn[TIMESTAMP] = mapped_column(
        TIMESTAMP,
        nullable=False,
        server_default=func.now()
    )
    persona = relationship("PersonaModel",back_populates="chats")