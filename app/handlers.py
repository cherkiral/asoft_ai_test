import asyncio
import logging

from aiogram import Router, F
from aiogram.types import Message


router = Router()

@router.message(F.text)
async def get_thread_handler(message: Message):
    logging.info(f"Пользователь прислал сообщение: {message.text}")

    waiting_msg = await message.answer("Бот думает 10 секунд")

    await asyncio.sleep(10)

    await message.answer(f"Дублированное сообщение пользователя: {message.text} ")

    logging.info(f"Бот продублировал сообщение: {message.text}")

    await waiting_msg.delete()