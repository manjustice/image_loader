import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import select, insert, exists

from app.core.database import async_session
from app.models import TelegramUser, Image
from config import TELEGRAM_BOT_TOKEN


bot = Bot(token=TELEGRAM_BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


async def save_image(image_path: str, image):
    os.makedirs("images", exist_ok=True)
    photo_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{image.file_path}"

    async with bot.session.get(photo_url) as response:
        response.raise_for_status()
        photo_data = await response.read()
        with open(image_path, 'wb') as f:
            f.write(photo_data)


async def create_data(
        user_id: int,
        username: str,
        image_url: str
):
    async with async_session() as db_session:
        user_query = (
            select(TelegramUser)
            .where(TelegramUser.id == user_id)
            .with_only_columns(TelegramUser.id)
        )
        response = await db_session.execute(user_query)

        user_exists = bool(response.scalar())

        if not user_exists:
            user = {
                "id": user_id,
                "username": username
            }
            query = insert(TelegramUser)
            await db_session.execute(query, user)
            await db_session.commit()

        image = {
            "url": image_url,
            "user_id": user_id
        }
        query = insert(Image)
        await db_session.execute(query, image)
        await db_session.commit()


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def handle_photo(message: types.Message):
    image_id = message.photo[-1].file_id
    image_path = os.path.join("images", f"{image_id}.jpg")

    image = await bot.get_file(image_id)
    await save_image(image_path, image)

    user_id = message.from_user.id
    username = message.from_user.username

    await create_data(user_id, username, image_path)

    await message.reply("I've saved your image")


async def main():
    await dp.start_polling()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
