import asyncio
import logging
from celery import shared_task
from aiogram import Bot
from app.bot.config import settings

@shared_task(name="worker.send_delayed_message")
def send_delayed_message(chat_id: int, text: str):

    logging.info(f"Celery получил сообщение: {chat_id}. Жду 10 секунд")

    async def send_message():
        bot = Bot(token=settings.BOT_TOKEN)
        try:
            waiting_msg = await bot.send_message(chat_id, "Бот думает 10 секунд")
            await asyncio.sleep(10)
            await waiting_msg.delete()
            await bot.send_message(chat_id, f"Дублированное сообщение: {text}")
        finally:
            await bot.session.close()

    asyncio.run(send_message())

    logging.info(f"Сообщение отправлено в чат {chat_id}")