from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models import TelegramUser


async def get_users(db_session: AsyncSession):
    query = select(TelegramUser).options(selectinload(TelegramUser.images))
    response = await db_session.execute(query)

    users = response.scalars().all()

    return users
