from aiogram.dispatcher.filters.state import State, StatesGroup


class UserState(StatesGroup):
    set_name = State()
    set_description = State()
    set_phone = State()
