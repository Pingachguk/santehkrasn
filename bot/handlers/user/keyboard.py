from aiogram import types


def start_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("📝 Заказать услуги сантехника"))
    markup.add(types.KeyboardButton("🔎 Узнать цены на услуги"))
    markup.add(types.KeyboardButton("📰 Канал с выполненными работами"))
    return markup