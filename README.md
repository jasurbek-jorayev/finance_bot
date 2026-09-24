# Finance Bot

Shaxsiy moliyani hisoblash uchun **Telegram bot**: kirim va chiqimlarni kategoriyalar bo'yicha yozib boring, statistika va tarixni ko'ring.

## Imkoniyatlar

- Tranzaksiya qo'shish: kirim yoki chiqim, summa va kategoriya
- Kategoriyalar ro'yxati
- Statistika: jami kirim, chiqim va balans
- Tranzaksiyalar tarixi
- Har bir foydalanuvchi ma'lumoti alohida

## Texnologiyalar

- **Python 3**, **aiogram 3** (Router, FSM)
- **PostgreSQL** + **asyncpg** (connection pool)

## Arxitektura

~~~
bot.py        # kirish nuqtasi
config.py     # sozlamalar (.env dan)
handlers/     # start, transactions, stats, history, categories
services/     # biznes logika: user, transaction, categories
db/           # ulanish (pool) va SQL so'rovlar
keyboards/    # tugmalar
~~~

## Ishga tushirish

~~~bash
pip install -r requirements.txt
cp .env.example .env
python bot.py
~~~

## Muhit o'zgaruvchilari

`BOT_TOKEN`, `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASS`