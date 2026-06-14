from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from db.connection import get_pool
from db.queries import add_transaction

from keyboards.inline import transaction_keyboard

router = Router()

class AddTransaction(StatesGroup):
    amount = State()

@router.message(F.text == "➕ Tranzaksiya qo'shish")
async def add_transaction_start(message: Message, state: FSMContext):
    await message.answer("Summani kiriting:", reply_markup=transaction_keyboard)
    await state.set_state(AddTransaction.amount)

@router.message(AddTransaction.amount)
async def save_transaction(message: Message, state: FSMContext):
    amount = message.text

    pool = get_pool()

    await add_transaction(
        pool,
        1,
        amount
    )

    await message.answer(
        f"✅ Bazaga saqlandi\n💰 {amount} so'm"
    )

    await state.clear()