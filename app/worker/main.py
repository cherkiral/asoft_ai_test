import logging
import asyncio
from app.worker.redis_config import redis_conn, queue
from rq import Worker, Queue
from rq.serializers import JSONSerializer
from aiogram import Bot
from app.bot.config import settings

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.BOT_TOKEN)

async def process_message(chat_id: int, text: str):
    logging.info(f"Обрабатываем сообщение для чата {chat_id}, ждём 10 секунд")
    await asyncio.sleep(10)
    await bot.send_message(chat_id, f"Дублированное сообщение: {text}")
    logging.info(f"Сообщение отправлено в чат {chat_id}")

if __name__ == "__main__":
    worker = Worker([queue], connection=redis_conn, serializer=JSONSerializer)
    worker.work()
