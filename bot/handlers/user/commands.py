import json
from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from .keyboard import start_keyboard

import requests


async def start(message: types.Message, state: FSMContext):
    markup = start_keyboard()
    await message.answer("Hello!", reply_markup=markup)

async def check_id(message: types.Message):
    await message.answer(message.chat.id)

async def clear_state(message: types.Message, state: FSMContext):
    await state.reset_state(True)
    await message.answer("Состояния очищены")

