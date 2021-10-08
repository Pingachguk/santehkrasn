import logging

from settings import config
from aiogram import Bot, Dispatcher, executor
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.contrib.fsm_storage.memory import BaseStorage
from db.cache import CacheRedis

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN, parse_mode="html")
storage = RedisStorage2('localhost', 6379)
dp = Dispatcher(bot, storage=storage)
cache = CacheRedis()


async def on_startup(dp):
    import handlers
    import middlewares
    import filters

    await bot.set_webhook(config.WEBHOOK_URL)

    await filters.setup(dp)
    await middlewares.setup(dp)
    await handlers.user.setup(dp)


async def on_shutdown(dp):
    print("[*] Bye")


if __name__ == '__main__':
    executor.start_webhook(
        dispatcher=dp,
        webhook_path=config.WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=config.WEBAPP_HOST,
        port=config.WEBAPP_PORT,
    )
