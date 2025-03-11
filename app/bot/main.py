import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
from app.bot.config import settings
from app.worker.redis_config import queue

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def handle_message(message: Message):
    logging.info(f"Получено сообщение от {message.chat.id}: {message.text}")

    queue.enqueue("app.worker.main.process_message", message.chat.id, message.text)

    await message.answer("Бот думает 10 секунд")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
