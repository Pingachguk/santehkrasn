from aiogram import types


def start_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton("📝 Заказать услуги сантехника"))
    markup.add(types.KeyboardButton("🔎 Узнать цены на услуги"))
    return markup