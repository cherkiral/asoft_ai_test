import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings
from handlers import router

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

async def main():
    logging.info("Бот запущен")

    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
