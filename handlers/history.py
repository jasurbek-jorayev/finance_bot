from aiogram import Router, F
from aiogram.types import Message

from db.connection import get_pool
from db.queries import get_transactions

router = Router()

@router.message(F.text == "📜 Tarix")
async def history(message: Message):
    pool = get_pool()

    rows = await get_transactions(pool)

    if not rows:
        await message.answer("Tarix bo'sh")
        return

    text = "📜 Oxirgi tranzaksiyalar:\n\n"

    for row in rows:
        text += f"💰 {row['amount']} | {row['created_at']}\n"

    await message.answer(text)