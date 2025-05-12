import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject # импортируем токен
import logging
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# Запускаем логгирование
# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
# )

# создаем диспетчер
dp = Dispatcher()
one = [[KeyboardButton(text='/баланс')],
       [KeyboardButton(text='/игрофон')],
       [KeyboardButton(text='/камерофон')],
       [KeyboardButton(text='/назад')]]
klava_one = ReplyKeyboardMarkup(keyboard=one, resize_keyboard=True, one_time_keyboard=True)

two = [[KeyboardButton(text='/только_глобальный_рынок')],
        [KeyboardButton(text='/с_китайский_рынком')],
       [KeyboardButton(text='/назад')]]
klava_two = ReplyKeyboardMarkup(keyboard=two, resize_keyboard=True, one_time_keyboard=True)

three = [[KeyboardButton(text='/новые')],
         [KeyboardButton(text='/б/у')],
         [KeyboardButton(text='/назад')]]
klava_three = ReplyKeyboardMarkup(keyboard=three, resize_keyboard=True, one_time_keyboard=True)
four = [[KeyboardButton(text='/- apple')],[KeyboardButton(text='/- samsung')],[KeyboardButton(text='/- xiaomi')],
         [KeyboardButton(text='/- poco')],[KeyboardButton(text='/- oneplus')],[KeyboardButton(text='/- realme')],
         [KeyboardButton(text='/- oppo')],[KeyboardButton(text='/- honor')],[KeyboardButton(text='/- huawey')],
         [KeyboardButton(text='/- vivo')], [KeyboardButton(text='/- iqoo')], [KeyboardButton(text='/оставить_все')],
         [KeyboardButton(text='/назад')], [KeyboardButton(text='/далее')]]
klava_four = ReplyKeyboardMarkup(keyboard=four, resize_keyboard=True, one_time_keyboard=True)
async def main():
    bot = Bot(token='7814578784:AAFEIg8-DKS1z6Lte7VGGa_lykNc1xy6GaM')
    await bot.delete_webhook()
    await dp.start_polling(bot)


@dp.message(Command('start'))  # декоратор для обработчика команды start

async def process_start_command(message: types.Message):
    """
    Создаем и регистрируем в диспетчере асинхронный обработчик сообщений.
    В параметре message содержится вся информация о сообщении - см. документацию.
    """
    await message.reply("Привет!\nЯ помогу выбрать вам телефон в популярном ценовом диапозоне от 25000 до "
                        "30000\nВыбирай:!", reply_markup=klava_one)  # отправляет ответ на сообщение



@dp.message(Command('help'))  # декоратор для обработчика команды help
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отправлю этот текст тебе в ответ!")

@dp.message(Command('назад'))
async def balance(message: types.Message):
    await message.reply('Вернулись назад :)', reply_markup=klava_one)

@dp.message(Command('баланс'))
async def balance(message: types.Message):
    await message.reply('b', reply_markup=klava_two)

@dp.message(Command('игрофон'))
async def game(message: types.Message):
    await message.reply('g', reply_markup=klava_two)

@dp.message(Command('камерофон'))
async def kamera(message: types.Message):
    await message.reply('k', reply_markup=klava_two)

@dp.message(Command('с_китайский_рынком'))
async def china(message: types.Message):
    await message.reply('c', reply_markup=klava_three)

@dp.message(Command('только_глобальный_рынок'))
async def globals(message: types.Message):
    await message.reply('g', reply_markup=klava_three)

@dp.message(Command('новые'))
async def new(message: types.Message):
    await message.reply('n', reply_markup=klava_four)

@dp.message(Command('б/у'))
async def use(message: types.Message):
    await message.reply('u', reply_markup=klava_four)

# @dp.message(Command('-'))
# async def delete(message: types.Message):
#     n = message.text.split('/-')[1]
#     print(four)
#     for el in four:
#         if el[0][0] == n:
#             four.remove(el[0][0])
#     await message.reply(f'{n}', reply_markup=klava_four)

@dp.message()  # декоратор для обработчика прочих сообщений
async def echo_message(message: types.Message):
    await message.answer(message.text)  # отправляет обратно новое сообщение с тем же текстом


if __name__ == '__main__':
    asyncio.run(main())  # начинаем принимать сообщения