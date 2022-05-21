from aiogram import  types
from aiogram.utils.callback_data import CallbackData



callback_commands = CallbackData('prefix', 'action')

async def cmd_test1(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Хочу рецепт", callback_data=callback_commands.new(action='get_recipe')))
    await message.answer("Приветствую! Чем могу помочь?", reply_markup=keyboard)


async def search_options(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Давай любой", callback_data=callback_commands.new(action='random_recipe')))
    keyboard.add(types.InlineKeyboardButton(text='Найди по названию', callback_data=callback_commands.new(action='order_by_name')))
    await call.message.answer('Окей, как будешь выбирать?', reply_markup=keyboard)
    await call.answer()
