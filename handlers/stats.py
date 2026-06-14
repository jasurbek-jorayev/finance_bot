from aiogram import Router, F
from aiogram.types import Message

from db.connection import get_pool
from db.queries import get_total_amount

router = Router()

@router.message(F.text == "📊 Statistika")
async def stats(message: Message):
    pool = get_pool()

    total = await get_total_amount(pool)

    await message.answer(
        f"📊 Umumiy summa: {total} so'm"
    )