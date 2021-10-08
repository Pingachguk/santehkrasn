from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Command, Text
from aiogram.types import ContentTypes
from . import commands, answers
from settings import config
from states.user.states import UserState


async def setup(dp: Dispatcher):
    # Clear states
    dp.register_message_handler(commands.clear_state, Command("reset"), state="*", is_private=True)

    # Commands
    dp.register_message_handler(commands.start, CommandStart(), is_private=True)
    dp.register_message_handler(commands.check_id, Command("checkid"), is_group=True)

    # Create order
    dp.register_message_handler(answers.set_name, Text("📝 Заказать услуги сантехника"), state=None, is_private=True)
    dp.register_message_handler(answers.set_description, state=UserState.set_name, is_private=True)
    dp.register_message_handler(answers.set_phone, state=UserState.set_description, is_private=True)
    dp.register_message_handler(answers.create_order, state=UserState.set_phone, is_private=True)
    dp.register_message_handler(answers.send_price, Text("🔎 Узнать цены на услуги"), state=None, is_private=True)
