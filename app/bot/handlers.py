import logging
from aiogram import Router, F
from aiogram.types import Message
from app.workers.tasks import send_delayed_message

router = Router()

@router.message(F.text)
async def get_thread_handler(message: Message):
    logging.info(f"Пользователь прислал сообщение: {message.text}")

    send_delayed_message.apply_async(args=[message.chat.id, message.text])

    logging.info(f"Сообщение '{message.text}' отправлено в Celery")
