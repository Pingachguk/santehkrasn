from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from requests.models import Response
from datetime import datetime
from settings import config
from states.user.states import UserState

import hashlib
import requests
import json


async def set_name(message: types.Message, state: FSMContext):
    await message.answer("Введите Ваше имя:")
    await state.set_state(UserState.set_name)

async def set_description(message: types.Message, state: FSMContext):
    await state.update_data(order_name=message.text)
    await message.answer("Опишите Вашу проблему:")
    await state.set_state(UserState.set_description)

async def set_phone(message: types.Message, state: FSMContext):
    await state.update_data(order_description=message.text)
    await message.answer("Введите Ваш номер телефона для связи:")
    await state.set_state(UserState.set_phone)

async def create_order(message: types.Message, state: FSMContext):
    await state.update_data(order_phone=message.text)
    data = await state.get_data()
    await message.answer("В ближайшее время с Вами свяжется наш специалист!")
    text_order = f"<b>Имя</b>: {data['order_name']}\n<b>Описание</b>:\n{data['order_description']}\n<b>Номер для связи</b>: {data['order_phone']}"
    await message.bot.send_message(chat_id=-767836134, text=text_order)
    await state.reset_state(False)

async def send_price(message: types.Message, state: FSMContext):
    await message.answer(config.PRICE_LIST)

async def send_channel(message: types.Message, state: FSMContext):
    await message.answer("Канал, где выкладываются выполненные работы и отзывы.\nhttps://t.me/Alexandrsantehnik_krasnodar")
