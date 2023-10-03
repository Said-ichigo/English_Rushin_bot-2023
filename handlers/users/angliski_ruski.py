from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.inline.english_inline import money_py,sub
from keyboards.default.lessons import Lessons
from keyboards.default.english_keybort import Memory


@dp.message_handler(Text(equals='Lessons 🧑‍🏫'))
async def lesson(message: types.Message):
    await message.answer('all lessons are here⬇️',reply_markup=Lessons)

@dp.message_handler(Text(equals='Lesson-1'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWqVhlC-2jYmz9JluLwUsyPe5DAbhiLwACMDEAAk7QWUgmJe1kdHcIxjAE'
                               f"ℹ️ Russian lessons – Lesson 1 – Tips, goals and Russian alphabet")

@dp.message_handler(Text(equals='Lesson-2'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWqTxlC-FgOaC2P7Cuis9288bqR5YhkAACTkEAAnVuWEirTlE-I6a_TzAE'
                               f"ℹ️ Russian lessons – Lesson 2 – Russian pronunciation. Personal pronouns")


@dp.message_handler(Text(equals='Lesson-3'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian lessons – Lesson 3 – Russian pronunciation mastery. Basic Russian phrases")

@dp.message_handler(Text(equals='Lesson-4'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian lessons – Lesson 4 – Russian nouns gender" )

@dp.message_handler(Text(equals='Lesson-5'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian language lesson 5 – Russian verbs conjugation")

@dp.message_handler(Text(equals='Lesson-6'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian lessons – Lesson 6 – Russian possessive pronouns")


@dp.message_handler(Text(equals='Lesson-7'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian lessons – Lesson 7 – Russian plurals")
    


@dp.message_handler(Text(equals='Lesson-8'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian sentence structure. Questions – Lesson 8")

@dp.message_handler(Text(equals='Lesson-9'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian adjectives – Russian lesson 9 – Russian language course")
    

@dp.message_handler(Text(equals='10'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian VERBS. Part 2 – Russian lesson 10 – Russian language course")


@dp.message_handler(Text(equals='Lesson-11'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian language practice – Russian lesson 11 – Russian language course")


@dp.message_handler(Text(equals='Lesson-12'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Negation in Russian – Russian Lesson 12 – Russian language")
    

@dp.message_handler(Text(equals='Lesson-13'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian cases – Russian lessons – Lesson 13")


@dp.message_handler(Text(equals='Lesson-14'))
async def engilish(message: types.Message):
    await message.answer_video('BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian cases – PREPOSITIONAL – Russian lessons – Lesson 14")


@dp.message_handler(Text(equals='Lesson-15'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian cases | PREPOSITIONAL-2 | Russian lessons | Lesson 15")
    

@dp.message_handler(Text(equals='Lesson-16'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Possession in Russian and VERBS+infinitive | Russian language")

@dp.message_handler(Text(equals='Lesson-17'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian adverbs – Lesson 17 – Russian Language Lesson")


@dp.message_handler(Text(equals='Lesson-18'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                               f"ℹ️ Russian dictation – Lesson 18 – Russian language")
    

@dp.message_handler(Text(equals='Lesson-19'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                              f"ℹ️ Accusative case — Lesson 19 From zero to fluency — Russian language")


@dp.message_handler(Text(equals='Lesson-20'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                            f"ℹ️ Past tense in Russian – Lesson 20 – From zero to Fluency")
    

@dp.message_handler(Text(equals='Lesson-21'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                            f"ℹ️ From Zero to Fluency – Lesson 21 – My FAMILY")
    

@dp.message_handler(Text(equals='Lesson-22'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                            f"ℹ️ DATIVE CASE Russian – From Zero to Fluency – Russian Lesson 22")

@dp.message_handler(Text(equals='Lesson-23'))
async def engilish(message: types.Message):
    await message.answer_video(video='BAACAgIAAxkBAAEWMmZk1hzxLGW2c2GNUi0DuNJdE4_QnwAC5TkAApvQsEoi5k9TZnw_FzAE'
                            f"ℹ️ How to use ТОЖЕ and ТАКЖЕ – From Zero to Fluency — Lesson 23")

##***********************************************************************************************************************##

@dp.message_handler(Text(equals='report to admin👨‍💻'))
async def lesson(message: types.Message):
    await message.answer(f"👀This is the telegram address of our admin."
                         "If you have any questionswrite to our admin👨‍💻",reply_markup=money_py)
    

@dp.message_handler(Text(equals='other bots with us🤖'))
async def Admin(message: types.Message):
    await message.answer(f"🤖If you<b>subscribe</b> to the channel,"
                        "you will receive <b>information</b> about clean bots ",parse_mode='HTML',reply_markup=sub)



    