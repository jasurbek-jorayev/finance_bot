from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

router = Router()

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="➕ Tranzaksiya qo'shish")],
        [KeyboardButton(text="📊 Statistika")],
        [KeyboardButton(text="📜 Tarix")],
        [KeyboardButton(text="📂 Kategoriyalar")]
    ],
    resize_keyboard=True
)

@router.message(CommandStart())
async def start_cmd(message: Message):
    await message.answer(
        "Finance Tracker Bot ga xush kelibsiz!",
        reply_markup=menu
    )