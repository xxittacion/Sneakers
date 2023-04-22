from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))

# Активация Dispatcher
dp = Dispatcher(bot=bot)

# Клавиатура
main = ReplyKeyboardMarkup(resize_keyboard=True).add('Контакты')

# Обработчик команды start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
  await message.answer_sticker('CAACAgIAAxkBAAMSZEQIb6F0CXsqitMen__vvH6Bt-QAAtgPAAJI8mBLFfvE2nh0a5gvBA') # отправить стикер
  await message.answer(f'{message.from_user.first_name}, рад вас видеть в магазине кроссовок.', reply_markup=main) # подключение клавиатуры

# Обработчки команд клавиатуры
@dp.message_handler(text='Контакты')
async def contacts(message: types.Message):
  await message.answer(f'По всем вопросам: @xxittacion')

# Обработчик неизвестных команд
@dp.message_handler()
async def answer(message: types.Message):
  await message.answer_sticker('CAACAgIAAxkBAAMaZEQJ3EURLRqonFGl5UxeIIso1SIAArwLAAL9F5lLRQUdiUsKeUcvBA')
  await message.reply(f'{message.from_user.first_name}, я вас не понимаю!')

# Обработчик стикеров, узнать id стикера: @idstickerbot
@dp.message_handler(content_types=['sticker'])
async def check_sticker(message: types.Message):
  await message.answer(message.sticker.file_id) # вернёт id стикера

if __name__ == '__main__':
  executor.start_polling(dp)
