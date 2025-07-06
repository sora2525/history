from typing import AsyncGenerator

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker,create_async_engine
from sqlalchemy.ext.asyncio.engine import AsyncEngine
import os

database_url = os.environ.get("DATABASE_URL")

def get_async_engine() -> AsyncEngine:
    return create_async_engine(url=database_url,echo=True)

def get_async_sessionmaker():
    return async_sessionmaker(
        bind=get_async_engine(),
        class_=AsyncSession,
        autocommit=False,
        autoflush=False,
        expire_on_commit=False,
    )

async def get_db() -> AsyncGenerator[AsyncSession,None]:
    async_session_local = get_async_sessionmaker()
    async with async_session_local() as session:
        try:
            yield session
        finally:
            await session.close()

