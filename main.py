from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))

# Активация Dispatcher
db = Dispatcher(bot=bot)

# Обработчик команды start
@db.message_handler(commands=['start'])
async def start(message: types.Message):
  await message.answer_sticker('CAACAgIAAxkBAAMSZEQIb6F0CXsqitMen__vvH6Bt-QAAtgPAAJI8mBLFfvE2nh0a5gvBA') # отправить стикер
  await message.answer(f'{message.from_user.first_name}, рад вас видеть в магазине кроссовок.')

# Обработчик неизвестных команд
@db.message_handler()
async def answer(message: types.Message):
  await message.answer_sticker('CAACAgIAAxkBAAMaZEQJ3EURLRqonFGl5UxeIIso1SIAArwLAAL9F5lLRQUdiUsKeUcvBA')
  await message.reply(f'{message.from_user.first_name}, я вас не понимаю!')

# Обработчик стикеров, узнать id стикера: @idstickerbot
@db.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
  await message.answer(message.sticker.file_id) # вернёт id стикера

if __name__ == '__main__':
  executor.start_polling(db)