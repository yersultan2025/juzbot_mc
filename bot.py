from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = "СЕНІҢ_БОТ_ТОКЕНІҢ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.reply("Сәлем! Мен жұмыс істеп тұрмын!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
