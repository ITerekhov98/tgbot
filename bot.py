import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.callback_data import CallbackData
from dotenv import load_dotenv

from tg_bot_app.handlers import common, named_recipe, rand_recipe

callback_commands = CallbackData('prefix', 'action')
logging.basicConfig(level=logging.INFO)

def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(common.cmd_test1, commands="start", state="*")
    dp.register_callback_query_handler(common.search_options, callback_commands.filter(action=['get_recipe']))

def register_handler_named_recipe(dp: Dispatcher):
    dp.register_message_handler(named_recipe.name_chosen, state=named_recipe.OrderRecipe.waiting_for_name)
    dp.register_callback_query_handler(named_recipe.order_by_name, callback_commands.filter(action=['order_by_name']))

def register_handler_rand_recipe(dp: Dispatcher):
    dp.register_callback_query_handler(rand_recipe.random_recipe, callback_commands.filter(action=['random_recipe']))

async def main():
    load_dotenv()
    token = os.getenv('TG_BOT_TOKEN')
    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())
    register_handlers_common(dp)
    register_handler_named_recipe(dp)
    register_handler_rand_recipe(dp)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())
