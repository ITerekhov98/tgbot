from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from tg_bot_app.db_functions import get_info_by_name
from tg_bot_app.bot_functions import response_formation


class OrderRecipe(StatesGroup):
    waiting_for_name = State()

async def order_by_name(call: types.CallbackQuery):
    await call.message.answer('Вводи название!')
    await OrderRecipe.waiting_for_name.set()
    await call.answer()

async def name_chosen(message: types.Message, state: FSMContext):
    chosen_name = message.text.lower()
    data = get_info_by_name(chosen_name)
    if data is None:
        await message.answer('Извини, такого не нашел. Попробуй другое название')
        return
    else:
        response = response_formation(data)
        await message.answer(response, parse_mode=types.ParseMode.MARKDOWN_V2)
        await state.finish()