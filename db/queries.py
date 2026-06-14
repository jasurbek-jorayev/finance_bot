async def add_user(pool, telegram_id, full_name):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO users(telegram_id, full_name)
            VALUES($1, $2)
            ON CONFLICT (telegram_id) DO NOTHING
            """,
            telegram_id,
            full_name
        )

async def add_transaction(pool, user_id, amount):
    async with pool.acquire() as conn:
        await conn.execute(
            """
            INSERT INTO transactions(user_id, amount)
            VALUES($1, $2)
            """,
            user_id,
            float(amount)
        )

async def get_transactions(pool):
    async with pool.acquire() as conn:
        return await conn.fetch(
            """
            SELECT amount, created_at
            FROM transactions
            ORDER BY id DESC
            LIMIT 10
            """
        )

async def get_total_amount(pool):
    async with pool.acquire() as conn:
        return await conn.fetchval(
            """
            SELECT COALESCE(SUM(amount), 0)
            FROM transactions
            """
        )