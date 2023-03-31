from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import filters
from func import regions, weather
import config



bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

def uzbekistan_regions_keyboard() -> types.ReplyKeyboardMarkup:
    buttons = [types.KeyboardButton(region) for region in regions]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(*buttons)
    return keyboard


    
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer('Assalomu alaykum!\n Bu bot orqali kunlik ob havo malumotlarini olishingiz mumkin!\n\nMarhamat viloyatingizni tanlang' , reply_markup=uzbekistan_regions_keyboard())


@dp.message_handler(content_types=['text'])
async def send_welcome(message: types.Message):
    if message.text in regions:
        a = weather(message.text)
        await message.answer(f'Siz tanlagan shahar: {message.text}🌆' + '\n\n' + a)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
