from aiogram import types

from tg_bot_app.db_functions import get_random_recipe
from tg_bot_app.bot_functions import response_formation

async def random_recipe(call: types.CallbackQuery):
    data = get_random_recipe()
    response = response_formation(data)
    await call.message.answer(response, parse_mode=types.ParseMode.MARKDOWN_V2)
    await call.answer()
