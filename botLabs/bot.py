from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from botsetting import keyboards as kb, stub_text

from labs.lab1 import compare_two_numbers
from botsetting.config import TOKEN
from botsetting.utils import TestStates

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(state='*', commands=['menu', 'start'])
async def process_start_command(message: types.Message):
    await set_state(message, 0)
    await message.reply(stub_text.MENU, reply_markup=kb.menu_kb)


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(stub_text.HELP)


@dp.message_handler(state=TestStates.TEST_STATE_0, commands=['lab1'])
async def process_help_command(message: types.Message):
    await message.reply(stub_text.LAB_1, reply_markup=kb.lab_1_kb)
    await set_state(message, 1)
    print(stub_text.LAB_1)


@dp.message_handler(state=TestStates.TEST_STATE_1)
async def compare_two_num(msg: types.Message):
    n = msg.text.split(' ')
    try:
        result = compare_two_numbers.compare(float(n[0]), float(n[1]))
        compare_two_numbers.compare(1,2)
        print(result)
        await bot.send_message(msg.from_user.id, result)
    except ValueError:
        await bot.send_message(msg.from_user.id, stub_text.LAB_1_ERROR)


@dp.message_handler(state=TestStates.TEST_STATE_0, commands=['lab2'])
async def process_help_command(message: types.Message):
    await message.reply(stub_text.LAB_2)
    print(stub_text.LAB_2)


@dp.message_handler(state=TestStates.TEST_STATE_0, commands=['lab3'])
async def process_help_command(message: types.Message):
    await message.reply(stub_text.LAB_3)
    print(stub_text.LAB_3)


async def set_state(message: types.Message, state: int):
    await dp.current_state(user=message.from_user.id).set_state(TestStates.all()[state])


if __name__ == '__main__':
    executor.start_polling(dp)
