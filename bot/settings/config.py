from dotenv import load_dotenv
import os

load_dotenv()  

API_TOKEN = os.getenv("BOT_TOKEN")


WEBAPP_HOST = "localhost"
WEBAPP_PORT = 3001

WEBHOOK_HOST = "https://add7-176-59-5-93.ngrok.io" 
WEBHOOK_PATH = "/path"
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}" 

PRICE_LIST = """
<b>Монтаж радиаторов отопления</b>: от 3 000 рублей 
<b>Монтаж душевой кабинки</b>: от 3 000 рублей 
<b>Установка и подключение стиральной машины</b>: от 1500 рублей 
<b>Установка и подключение посудомоечной машины</b>: от 1500 рублей 
<b>Монтаж унитаза</b>: от 1500 руб
<b>Монтаж инсталляции</b>: от 3000 рублей 
<b>Замена смесителя</b>: от 1500 рублей 
<b>Ванная под ключ ЭКОНОМ ВАРИАНТ</b>: от 40. 000 рублей
"""
