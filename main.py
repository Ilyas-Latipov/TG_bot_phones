import asyncio
import sqlite3 as sl
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandObject  # импортируем токен
import logging
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

# создаем диспетчер
bot = Bot(token='7814578784:AAFEIg8-DKS1z6Lte7VGGa_lykNc1xy6GaM')
dp = Dispatcher()

one = [[KeyboardButton(text='/+ баланс')],
       [KeyboardButton(text='/+ игрофон')],
       [KeyboardButton(text='/+ камерофон')],
       [KeyboardButton(text='/назад')]]
klava_one = ReplyKeyboardMarkup(keyboard=one, resize_keyboard=True, one_time_keyboard=True)

two = [[KeyboardButton(text='/только_глобальный_рынок')],
       [KeyboardButton(text='/с_иностранным_рынком')],
       [KeyboardButton(text='/назад')]]
klava_two = ReplyKeyboardMarkup(keyboard=two, resize_keyboard=True, one_time_keyboard=True)

three = [[KeyboardButton(text='/только_новые')],
         [KeyboardButton(text='/можно и б\у')],
         [KeyboardButton(text='/назад')]]
klava_three = ReplyKeyboardMarkup(keyboard=three, resize_keyboard=True, one_time_keyboard=True)

four = [[KeyboardButton(text='/- apple')], [KeyboardButton(text='/- samsung')], [KeyboardButton(text='/- xiaomi')],
        [KeyboardButton(text='/- poco')], [KeyboardButton(text='/- oneplus')], [KeyboardButton(text='/- realme')],
        [KeyboardButton(text='/- oppo')], [KeyboardButton(text='/- honor')], [KeyboardButton(text='/- vivo')],
        [KeyboardButton(text='/- iqoo')], [KeyboardButton(text='/- pixel')], [KeyboardButton(text='/- huawei')],
        [KeyboardButton(text='/далее')], [KeyboardButton(text='/назад')]]
klava_four = ReplyKeyboardMarkup(keyboard=four, resize_keyboard=True, one_time_keyboard=True)

start = [[KeyboardButton(text='/start')]]
klava_start = ReplyKeyboardMarkup(keyboard=start, resize_keyboard=True, one_time_keyboard=True)

end = [[KeyboardButton(text='/оставить_отзыв')], [KeyboardButton(text='/назад')]]
klava_end = ReplyKeyboardMarkup(keyboard=end, resize_keyboard=True, one_time_keyboard=True)

exit = []
delt = ''
fd = False
recomendation = 0
KEY = 'amol'


async def main():
    await bot.delete_webhook()
    await dp.start_polling(bot)


@dp.message(Command('start'))  # декоратор для обработчика команды start
async def process_start_command(message: types.Message):
    global recomendation, delt
    recomendation = 0
    delt = ''
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
    global exit, delt, recomendation
    exit = []
    delt = ''
    recomendation = 0
    await message.reply('Вернулись назад :)\n/start', reply_markup=klava_start)


@dp.message(Command('+'))
async def balance(message: types.Message):
    global exit
    if exit == [] and len(message.text.split('/+ ')) > 1:
        exit.append(message.text.split('/+ ')[1])
    elif len(exit) >= 1:
        exit[0] = message.text.split('/+ ')[1]
    await message.reply('Теперь выберите для какого рынка вам нужет смартфон:\n\n'
                        'Глобальный рынок - рынок для всего мира, поддерживает все бэнды (связь ловит по максимуму'
                        ':) ) и все языки. Легкая настройка.\n\n'
                        'Иностранный рынок - открывает двери к смартфонам цена/качество. Поддерживает не все бэнды'
                        '(ловит чуть хуже). Почти везде есть поддержка русского языка и везде английского языка.'
                        'Чтобы его настроить придется повозиться :). Телефон может прийти перепрошитым под '
                        'глобальную версию (система от глобальной версии со всеми языками и легкой настройкой, но '
                        'бэндов не прибавится). За все эти муки смартфоны обходятся по низкой цене :). Доставка так же '
                        'из за рубежа и если придет брак, то отправить его обратно будет не просто. Так же некоторые '
                        'китайские смартфоны в китайской версии имеют лучшую оболочку, чем в глобальной версии ;)',
                        reply_markup=klava_two)


@dp.message(Command('с_иностранным_рынком'))
async def china(message: types.Message):
    global exit
    if len(exit) == 1:
        exit.append('не глобал')
    elif len(exit) >= 2:
        exit[1] = 'не глобал'
    await message.reply('Теперь решите в каком состоянии вы выбираете телефон:\n\n'
                        'Новый - ничего лишнего, абсолютно новый телефон в коробке.\n\n'
                        'Б/у (использованный) - телефон мог побывать в ремонте, или быть старой моделью в идеальном '
                        'состоянии, или быть разбитым. Вы покупаете кота в мешке, но цена тут гораздо ниже, чем у новых,'
                        'а также есть прошлогодние флагманы по хорошей цене :)', reply_markup=klava_three)


@dp.message(Command('только_глобальный_рынок'))
async def globals(message: types.Message):
    global exit
    if len(exit) == 1:
        exit.append('глобал')
    elif len(exit) >= 2:
        exit[1] = 'глобал'
    await message.reply('Теперь решите в каком состоянии вы выбираете телефон:\n\n'
                        'Новый - ничего лишнего, абсолютно новый телефон в коробке.\n\n'
                        'Б/у (использованный) - телефон мог побывать в ремонте, или быть старой моделью в идеальном '
                        'состоянии, или быть разбитым. Вы покупаете кота в мешке, но цена тут гораздо ниже, чем '
                        'у новых, а также есть прошлогодние флагманы по хорошей цене :)', reply_markup=klava_three)


@dp.message(Command('только_новые'))
async def new(message: types.Message):
    global exit
    if len(exit) == 2:
        exit.append('новый')
    elif len(exit) >= 3:
        exit[2] = 'новый'
    await message.reply('Теперь исключите все марки смартфонов которые вы не хотите видеть у себя в рекомендации,'
                        'а потом нажмите /далее и ваш список готов :). Если вы хотите увидеть всех - просто нажмите '
                        '/далее', reply_markup=klava_four)


@dp.message(Command('можно'))
async def use(message: types.Message):
    global exit
    if len(exit) == 2:
        exit.append('новыйб/у')
    elif len(exit) >= 3:
        exit[2] = 'новыйб/у'
    await message.reply('Теперь исключите все марки смартфонов которые вы не хотите видеть у себя в рекомендации,'
                        'а потом нажмите /далее и ваш список готов :). Если вы хотите увидеть всех - просто нажмите '
                        '/далее', reply_markup=klava_four)


@dp.message(Command('-'))
async def delete(message: types.Message):
    global delt
    if len(message.text.split('/- ')) > 1:
        mark = message.text.split('/- ')[1]
        delt += f'{mark} '
        await message.reply(f'Вы исключили марку - {mark}\n\n'
                            f'Все исключенные марки смартфонов: {delt}', reply_markup=klava_four)
    else:
        await message.reply('Вы не написали марку', reply_markup=klava_four)


@dp.message(Command('далее'))
async def use(message: types.Message):
    global recomendation
    recomendation = 0
    baza = sl.connect('phons_db.db')
    cur = baza.cursor()
    phons_in = cur.execute("SELECT * FROM phons_in")
    # Добавление даных из базы в выводной лист
    if len(exit) == 3:
        for row in phons_in:
            if exit != []:
                if exit[0] in row[4] and row[5] in exit[1] and row[6] in exit[2] and row[0][:5] not in delt:
                    recomendation += 1
                    await message.answer(f'{recomendation}. Вам может подойти:\n\n{row[1]}\nКлассификация: '
                                         f'{row[4]}, {row[5]}, {row[6]}\n\n', reply_markup=klava_end)
                    await message.answer_photo(photo=f'{row[2]}')
                    await message.answer('-')
    # Отключение от бызы данных
    baza.close()

    if recomendation == 0:
        await message.reply(f'У вас нет рекомендованных смартфонов :(', reply_markup=klava_end)


@dp.message(Command('оставить_отзыв'))
async def add_feedback(message: types.Message):
    global fd
    fd = True
    await message.answer('Пишите ваш отзыв ;)', reply_markup=klava_start)


@dp.message(Command('add'))
async def add(message: types.Message):
    elem = message.text.split('; ')
    if elem[0][5:9] == KEY:
        baza = sl.connect('phons_db.db')
        cur = baza.cursor()
        # Добавление данных в базу
        cur.execute(f'INSERT INTO phons_in (name, descript, url, price, clas, market, condition) '
                    f'values(?, ?, ?, ?, ?, ?, ?)',
                    (elem[0][10:], elem[1], elem[2], elem[3], elem[4], elem[5], elem[6]))
        # Сохранение изменений в базе
        baza.commit()
        await message.answer('Успешно :)', reply_markup=klava_start)
    else:
        await message.answer('Неправильный ключ доступа после /add :(',
                             reply_markup=klava_start)


@dp.message(Command('read'))
async def read(message: types.Message):
    elem = message.text.split()
    elem.append('')
    if elem[1] == KEY:
        await message.answer('Смотрите :)', reply_markup=klava_start)
        baza = sl.connect('feedback_db.db')
        cur = baza.cursor()
        feedbacks = cur.execute("SELECT * FROM feedbacks")
        for row in feedbacks:
            await message.answer(row[1], reply_markup=klava_start)
    else:
        await message.answer('Неправильный ключ доступа после /read :(',
                             reply_markup=klava_start)


@dp.message(Command('clear'))
async def clear(message: types.Message):
    elem = message.text.split()
    elem.append('')
    if elem[1] == KEY:
        # Подключение бызы данных
        baza = sl.connect('feedback_db.db')
        cur = baza.cursor()
        # Удаление данныз в базе
        cur.execute('DELETE from feedbacks')
        # Сохранение изменений в базе
        baza.commit()
        # Отключение от бызы данных
        baza.close()
        await message.answer('Отзывы удаленны из БД', reply_markup=klava_start)
    else:
        await message.answer('Неправильный ключ доступа после /clear :(',
                             reply_markup=klava_start)


@dp.message(F.photo)
async def foto_url(message: types.Message):
    photo_data = f'{message.photo[-1]}'
    photo_data = photo_data.split("'")[1]
    await message.answer(f'{photo_data}')


@dp.message()  # декоратор для обработчика прочих сообщений
async def echo_message(message: types.Message):
    global fd
    if fd:
        txt = message.text
        baza = sl.connect('feedback_db.db')
        cur = baza.cursor()
        # Добавление данных в базу
        cur.execute(f'INSERT INTO feedbacks (text)'
                    f'values(?)', (txt,))
        # Сохранение изменений в базе
        baza.commit()
        fd = False
        await message.answer('Спасибо! :)', reply_markup=klava_start)
    else:
        await message.answer('Максимум что вам надо писать в чат это команду /start, а остальное - кнопки:)')


if __name__ == '__main__':
    asyncio.run(main())
    # начинаем принимать сообщения
