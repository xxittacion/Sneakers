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
  await message.answer(f'{message.from_user.first_name}, добро пожаловать в магазин кроссовок.')

# Обработчик неизвестных сообщений и команд
@db.message_handler()
async def answer(message: types.Message):
  await message.reply(f'{message.from_user.first_name}, я вас не понимаю!')

if __name__ == '__main__':
  executor.start_polling(db)