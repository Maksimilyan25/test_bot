import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command

from constants import (
    TEXT_CLEN,
    TEXT_MASTER_CLASS,
    TEXT_PROJECT,
    TEXT_RUSSIAN_PROJECT,
    FILE_URL,
    FILE_CREATE_AGENT,
    FILE_CREATE_NUM,
    FILE_CREATE_OUT_ORDER,
    FILE_INGREDIENTS,
    FILE_ORDER,
    FILE_RETURN_ORDER,
    FILE_ROS
)

dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: types.Message) -> None:
    kb = [
        [types.InlineKeyboardButton(
            text='1C',
            callback_data='get_one_c')],
        [types.InlineKeyboardButton(
            text='Рекламации',
            callback_data='сomplaint')],
        [types.InlineKeyboardButton(
            text='База знаний',
            callback_data='database')],
        [types.InlineKeyboardButton(
            text='Сервисное обслуживание оборудования',
            callback_data='service_device')],
        [types.InlineKeyboardButton(
            text='О компании',
            callback_data='company_info')],
        [types.InlineKeyboardButton(
            text='Проверка вложенности',
            callback_data='nesting')],
        [types.InlineKeyboardButton(
            text='Техническая поддержка',
            callback_data='support')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer(
        'Здравствуйте, что бы вы хотели узнать?', reply_markup=keyboard)


@dp.callback_query(F.data == 'get_one_c')
async def get_one_c(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='Создание Заказа покупателя и выставление счёта',
            callback_data='create_order')],
        [types.InlineKeyboardButton(
            text='Создание отгрузочной накладной',
            callback_data='create_out_document')],
        [types.InlineKeyboardButton(
            text='Возврат от покупателя',
            callback_data='return_order')],
        [types.InlineKeyboardButton(
            text='Создание контрагента',
            callback_data='create_agent')],
        [types.InlineKeyboardButton(
            text='Создание номенклатуры',
            callback_data='create_nomenclaturs')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'create_order')
async def create_order(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.delete()
    with open(FILE_ORDER, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Создание_Заказа_и_выставление_счёта.pdf'
            ),
            caption='Вот документ для изучения '
            'Создание Заказа Покупателя и выставление счёта.',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'create_out_document')
async def create_out_document(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_CREATE_OUT_ORDER, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Создание отгрузочной накладной.pdf'
            ),
            caption='Вот документ для изучения '
            'Создание отгрузочной накладной',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'return_order')
async def return_order(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_RETURN_ORDER, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Возврат от покупателя.pdf'
            ),
            caption='Вот документ для изучения '
            'Возврат от покупателя',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'create_agent')
async def create_agent(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_CREATE_AGENT, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Создание контрагента.pdf'
            ),
            caption='Вот документ для изучения Создание контрагента',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'create_nomenclaturs')
async def create_nomenclaturs(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_CREATE_NUM, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Создание номенклатуры.pdf'
            ),
            caption='Вот документ для изучения Создание номенклатуры',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'сomplaint')
async def сomplaint(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='Клён',
            callback_data='get_clen')],
        [types.InlineKeyboardButton(
            text='Рестинтернешнл',
            callback_data='restinternation')],
        [types.InlineKeyboardButton(
            text='Мастеркласс',
            callback_data='master_of_class')],
        [types.InlineKeyboardButton(
            text='Регион 50(Проект 2015)',
            callback_data='region_and_project')],
        [types.InlineKeyboardButton(
            text='Русский проект (метроном)',
            callback_data='russian_project')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='back')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'get_clen')
async def get_clen(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(TEXT_CLEN, reply_markup=keyboard)


@dp.callback_query(F.data == 'restinternation')
async def restinternation(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Вот документ для изучения Рестинтернешнл', reply_markup=keyboard)
    with open(FILE_ROS, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Рестинтернешнл.docx'
            ),
            caption='Вот документ для изучения Рестинтернешнл',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'master_of_class')
async def master_of_class(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(TEXT_MASTER_CLASS, reply_markup=keyboard)


@dp.callback_query(F.data == 'region_and_project')
async def region_and_project(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(TEXT_PROJECT, reply_markup=keyboard)


@dp.callback_query(F.data == 'russian_project')
async def russian_project(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        TEXT_RUSSIAN_PROJECT, reply_markup=keyboard)


@dp.callback_query(F.data == 'database')
async def database(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='Барный инвентарь',
            callback_data='bar_inventory')],
        [types.InlineKeyboardButton(
            text='Сиропы, топинги, пюре',
            callback_data='ingredients')],
        [types.InlineKeyboardButton(
            text='Оборудование',
            callback_data='equipment')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='back')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'bar_inventory')
async def bar_inventory(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_URL, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Бар инвентарь.pdf'
            ),
            caption='Вот документ для изучения Барный инвентарь',
            reply_markup=keyboard
        )


@dp.callback_query(F.data == 'ingredients')
async def ingredients(callback: types.CallbackQuery, bot: Bot):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    with open(FILE_INGREDIENTS, 'rb') as file:
        await bot.send_document(
            chat_id=callback.message.chat.id,
            document=types.BufferedInputFile(
                file.read(),
                filename='Сиропы, топинги, пюре.pdf'
            ),
            caption='Вот документ для изучения Сиропы, топинги, пюре',
            reply_markup=keyboard
        )


@dp.message(F.text == 'equipment')
async def equipment(message: types.Message):
    await message.answer('Ожидайте...😊')


@dp.callback_query(F.data == 'service_device')
async def service_device(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='database')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'company_info')
async def company_info(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='database')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'nesting')
async def nesting(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='Первый', callback_data='first')],
        [types.InlineKeyboardButton(
            text='Второй', callback_data='second')],
        [types.InlineKeyboardButton(
            text='Третий', callback_data='third')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='database')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'first')
async def first(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='ПодПодКатегория', callback_data='first_first')],
        [types.InlineKeyboardButton(
            text='2ПодПодКатегория', callback_data='second_second')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='nesting')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'first_first')
async def first_first(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='Еще вложение', callback_data='first_more')],
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='first')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'first_more')
async def first_more(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Просто проверка, ничего важного', reply_markup=keyboard)


@dp.callback_query(F.data == 'second')
async def second(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Просто проверка, ничего важного', reply_markup=keyboard)


@dp.message(F.text == 'third')
async def third(message: types.Message):
    await message.answer('Ожидайте...😊')


@dp.callback_query(F.data == 'support')
async def support(callback: types.CallbackQuery):
    kb = [
        [types.InlineKeyboardButton(
            text='<<Назад', callback_data='back')],
        [types.InlineKeyboardButton(
            text='В меню↩️', callback_data='back_to_menu')]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await callback.message.edit_text(
        'Выберите подкатегорию', reply_markup=keyboard)


@dp.callback_query(F.data == 'back_to_menu')
async def back_to_menu_handler(callback: types.CallbackQuery):
    await callback.message.delete()
    await start_command(callback.message)


async def main() -> None:
    token = '7961373534:AAE8y1ezZza9ZfQLUQrw4jlAwn8LlPDHsCk'
    bot = Bot(token)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
