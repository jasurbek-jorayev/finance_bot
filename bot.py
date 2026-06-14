import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from db.connection import create_pool

from handlers.start import router as start_router
import handlers.transactions

from handlers.stats import router as stats_router

from handlers.history import router as history_router

from handlers.categories import router as categories_router


async def main():
    bot = Bot(token=BOT_TOKEN)

    dp = Dispatcher()

    await create_pool()

    dp.include_router(start_router)
    dp.include_router(handlers.transactions.router)
    dp.include_router(stats_router)
    dp.include_router(history_router)
    dp.include_router(categories_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())