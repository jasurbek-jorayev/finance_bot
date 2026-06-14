from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

transaction_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="➕ Kirim",
                callback_data="income"
            ),
            InlineKeyboardButton(
                text="➖ Chiqim",
                callback_data="expense"
            )
        ]
    ]
)