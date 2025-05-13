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
bot = Bot(token='7814578784:AAFEIg8-DKS1z6Lte7VGGa_lykNc1xy6GaM')
dp = Dispatcher()

one = [[KeyboardButton(text='/+ баланс')],
       [KeyboardButton(text='/+ игрофон')],
       [KeyboardButton(text='/+ камерофон')],
       [KeyboardButton(text='/назад')]]
klava_one = ReplyKeyboardMarkup(keyboard=one, resize_keyboard=True, one_time_keyboard=True)

two = [[KeyboardButton(text='/только_глобальный_рынок')],
        [KeyboardButton(text='/с_китайский_рынком')],
       [KeyboardButton(text='/назад')]]
klava_two = ReplyKeyboardMarkup(keyboard=two, resize_keyboard=True, one_time_keyboard=True)

three = [[KeyboardButton(text='/только_новые')],
         [KeyboardButton(text='/можно и б\у')],
         [KeyboardButton(text='/назад')]]
klava_three = ReplyKeyboardMarkup(keyboard=three, resize_keyboard=True, one_time_keyboard=True)
four = [[KeyboardButton(text='/- apple')],[KeyboardButton(text='/- samsung')],[KeyboardButton(text='/- xiaomi')],
         [KeyboardButton(text='/- poco')],[KeyboardButton(text='/- oneplus')],[KeyboardButton(text='/- realme')],
         [KeyboardButton(text='/- oppo')],[KeyboardButton(text='/- honor')], [KeyboardButton(text='/- vivo')],
         [KeyboardButton(text='/- iqoo')], [KeyboardButton(text='/- pixel')],
         [KeyboardButton(text='/далее')], [KeyboardButton(text='/назад')]]
klava_four = ReplyKeyboardMarkup(keyboard=four, resize_keyboard=True, one_time_keyboard=True)
start = [[KeyboardButton(text='/start')]]
klava_start = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, one_time_keyboard=True)
end = [[KeyboardButton(text='/оставить_отзыв')], [KeyboardButton(text='/start')]]
klava_end = ReplyKeyboardMarkup(keyboard=end, resize_keyboard=True, one_time_keyboard=True)

phons = ['apple - 13 б/у, баланс', 'samsung - s23 китай, new, баланс-камерофон',
         'samsung - s23Fe баланс-камерофон', 'samsung - s22 Ultra б/у, баланс-камерофон',
         'xiaomi - 13T Pro баланс', 'xiaomi - 14T баланс-камерофон', 'xiaomi - 12S Ultra б/у, баланс-камерофон',
         'xiaomi - 11Ultra камерофон', 'xiaomi - 13 китай, new, баланс-камерофон',
         'xiaomi - K70 Ultra китай, new, игрофон', 'poco - X7 Pro игрофон', 'oneplus - 11 баланс-камерофон',
         'oneplus - Ace 5 китай, new, игрофон', 'realme - 14 Pro+ камерофон', 'realme - Neo 7 китай, new, игрофон',
         'realme - GT6 китай, б/у, игрофон', 'oppo - Find X6 Pro китай, б/у, баланс-камерофон', 'honor - 200 камерофон',
         'honor - 200 Pro китай, new, камерофон', 'honor - GT китай, new, игрофон',
         'vivo - X90 Pro+ китай, б/у, баланс-камерофон', 'iqoo - 12 китай, б/у, баланс',
         'iqoo - Neo 9s Pro+ китай, new, баланс', 'iqoo - Neo 10 китай, new, игрофон', 'pixel - 7 pro б/у, камерофон']
exit = []
clas = ''

async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)


@dp.message(Command('start'))  # декоратор для обработчика команды start

async def process_start_command(message: types.Message):
    """
    Создаем и регистрируем в диспетчере асинхронный обработчик сообщений.
    В параметре message содержится вся информация о сообщении - см. документацию.
    """
    await message.reply("Привет!\nЯ помогу выбрать вам телефон в популярном ценовом диапозоне от 25000 до "
                        "30000 рублей\n\nВыбери классификацию смартвона (для каких целей он нужен):\n\n"
                        "Баланс: сбалансированные смартфоны. Хорошие как для игр, так и для фотографий,\n\n"
                        "Игрофон: игровые смартфоны. Тянут все игры на хороших настройках. Не тормозят в системе.\n\n"
                        "Камерафон: смартфоны для фотографий. Хорошие камеры с оптическим приближением.",
                        reply_markup=klava_one)  # отправляет ответ на сообщение



@dp.message(Command('help'))  # декоратор для обработчика команды help
async def process_help_command(message: types.Message):
    await message.reply("Привет!\nЯ помогу выбрать вам телефон в популярном ценовом диапозоне от 25000 до "
                        "30000 рублей\n\nМаксимум что вам надо писать в чат это команду /start, а остальное - кнопки:)")

@dp.message(Command('назад'))
async def out(message: types.Message):
    global exit, clas
    exit = []
    clas = ''
    await message.reply('Вернулись назад :)\n/start', reply_markup=klava_start)

@dp.message(Command('+'))
async def balance(message: types.Message):
    global clas
    category = message.text.split('/+ ')[1]
    clas = category
    print(category)
    for el in phons:
        if category in el.split()[-1] and 'китай' not in el.split()[-3] and 'б/у' not in el.split()[-2]:
            exit.append(el)
    print(exit)
    await message.reply('Теперь выберите для какого рынка вам нужет смартфон:\n\n'
                        'Глобальный рынок - рынок для всего мира, поддерживает все бэнды (связь ловит по максимуму'
                        ':) ) и все языки. Легкая настройка.\n\n'
                        'Китайский рынок - открывает двери к смартфонам цена/качество. Поддерживает не все бэнды'
                        '(ловит чуть хуже). Почти везде есть поддержка русского языка и везде английского языка.'
                        'Чтобы его настроить придется повозиться :). Телефон может прийти перепрошитым под '
                        'глобальную версию (система от глобальной версии со всеми языками и легкой настройкой, но '
                        'бэндов не прибавится). За все эти муки смартфоны обходятся по низкой цене :). Доставка так же '
                        'из Китая и если придет брак, то отправить его обратно будет не просто. Так же некоторые '
                        'смартфоны в китайской версии имеют лучшую оболочку, чем в глобальной версии ;)', reply_markup=klava_two)

@dp.message(Command('с_китайский_рынком'))
async def china(message: types.Message):
    print(clas)
    for el in phons:
        if 'китай' in el.split()[-3] and clas in el.split()[-1] and 'б/у' not in el.split()[-2]:
            exit.append(el)
    print(exit)
    await message.reply('Теперь решите в каком состоянии вы выбираете телефон:\n\n'
                        'Новый - ничего лишнего, абсолютно новый телефон в коробке.\n\n'
                        'Б/у (использованный) - телефон мог побывать в ремонте, или быть старой моделью в идеальном '
                        'состоянии, или быть разбитым. Вы покупаете кота в мешке, но цена тут гораздо ниже, чем у новых,'
                        'а также есть прошлогодние флагманы по хорошей цене :)', reply_markup=klava_three)

@dp.message(Command('только_глобальный_рынок'))
async def globals(message: types.Message):
    await message.reply('Теперь решите в каком состоянии вы выбираете телефон:\n\n'
                        'Новый - ничего лишнего, абсолютно новый телефон в коробке.\n\n'
                        'Б/у (использованный) - телефон мог побывать в ремонте, или быть старой моделью в идеальном '
                        'состоянии, или быть разбитым. Вы покупаете кота в мешке, но цена тут гораздо ниже, чем '
                        'у новых, а также есть прошлогодние флагманы по хорошей цене :)', reply_markup=klava_three)

@dp.message(Command('только_новые'))
async def new(message: types.Message):
    await message.reply('Теперь исключите все марки смартфонов которые вы не хотите видеть у себя в рекомендации,'
                        'а потом нажмите /далее и ваш список готов :). Если вы хотите увидеть всех - просто нажмите '
                        '/далее', reply_markup=klava_four)

@dp.message(Command('можно'))
async def use(message: types.Message):
    for el in phons:
        if 'б/у' in el.split()[-2] and clas in el.split()[-1]:
            exit.append(el)
    print(exit)
    await message.reply('Теперь исключите все марки смартфонов которые вы не хотите видеть у себя в рекомендации,'
                        'а потом нажмите /далее и ваш список готов :). Если вы хотите увидеть всех - просто нажмите '
                        '/далее', reply_markup=klava_four)

@dp.message(Command('-'))
async def delete(message: types.Message):
    mark = message.text.split('/- ')[1]
    delt = []
    text = f'{mark}'
    for el in exit:
        if el.split()[0] == mark:
            delt.append(el)
    if delt == []:
        text = 'этой марки уже нет в списке рекомендаций'
    if exit == []:
        text = 'у вас нет рекомендованных смартфонов :('
    for el in delt:
        exit.remove(el)
    print(exit)
    await message.reply(f'Вы исключили марку - {text}', reply_markup=klava_four)

@dp.message(Command('далее'))
async def use(message: types.Message):
    end = '\n'.join(exit)
    media = types.MediaGroup()
    media.attach_photo(types.InputFile('Рабочий стол/media/apple - 13.jpg'), 'apple - 13')
    await message.reply_media_group(media=media)
    await message.reply(f'Вам может подойти:\n\n{end}', reply_markup=klava_end)

# def addbd():
#         # Подключение бызы данных
#     baza = sl.connect('l1.db')
#     cur = baza.cursor()
#     game = cur.execute("SELECT * FROM games")
#     # Добавление даных из базы в выводной лист
#     for row in game:
#         name = row[0]
#         text = row[1],
#         url = row[2]
#         for el in exit:
#             if el.split(';')[0] == name:
#                 message.reply(f'Вам может подойти:\n\n{end}', reply_markup=klava_end)
#     # Отключение от бызы данных
#     baza.close()

@dp.message()  # декоратор для обработчика прочих сообщений
async def echo_message(message: types.Message):
    await message.answer('Максимум что вам надо писать в чат это команду /start, а остальное - кнопки:)')  # отправляет обратно новое сообщение с тем же текстом


if __name__ == '__main__':
    asyncio.run(main())
    # начинаем принимать сообщения