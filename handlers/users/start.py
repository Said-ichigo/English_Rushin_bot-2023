from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text 
from keyboards.default.english_keybort import Memory

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"This is the menu section {message.from_user.full_name}",
                         reply_markup=Memory)

@dp.message_handler(Text(equals='help us with money💳'))
async def tolew_uz(message: types.Message, state:FSMContext):
    await message.answer(f"<code>8600061010547833</code>"
                              '👈you can easily put money on this plastic card☺️', parse_mode='HTML')
    
@dp.message_handler(Text(equals='⬅️Back to menu'))
async def back_menu(message: types.Message):
    await message.answer('Main menu👇',reply_markup=Memory)