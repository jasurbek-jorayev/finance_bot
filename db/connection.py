import asyncpg
from config import *

pool = None

async def create_pool():
    global pool

    pool = await asyncpg.create_pool(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

    return pool

def get_pool():
    return pool