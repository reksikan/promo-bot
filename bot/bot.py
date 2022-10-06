from aiogram import Bot, Dispatcher, types, executor
import requests

from config import BOT_TOKEN
import textes as text

bot = Bot(BOT_TOKEN)
dispatcher = Dispatcher(bot)

@dispatcher.message_handler(commands=('start', ))
async def start(message: types.Message):
    await message.answer(
        text=text.TEXT_RU_START,
    )

@dispatcher.message_handler(content_types=(types.ContentTypes.PHOTO, ))
async def send_promo(message: types.Message):
    await message.answer(
        text=text.TEXT_RU_SENDPROMO
    )\

@dispatcher.message_handler(lambda message: message.photo is None)
async def send_promo(message: types.Message):
    await message.answer(
        text=text.TEXT_RU_MISTAKE
    )

if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)