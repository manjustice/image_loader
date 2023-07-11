from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import async_session


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
