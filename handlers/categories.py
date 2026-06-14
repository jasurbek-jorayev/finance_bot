from aiogram import Router, F
from aiogram.types import Message

router = Router()

categories = [
    "🍔 Oziq-ovqat",
    "🚕 Transport",
    "🎮 Ko'ngilochar",
    "📚 Ta'lim"
]

@router.message(F.text == "📂 Kategoriyalar")
async def show_categories(message: Message):
    text = "📂 Kategoriyalar:\n\n"

    for cat in categories:
        text += f"{cat}\n"

    await message.answer(text)