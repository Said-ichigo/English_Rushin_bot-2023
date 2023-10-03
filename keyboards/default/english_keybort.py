from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

Memory = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Lessons 🧑‍🏫'),
            KeyboardButton('report to admin👨‍💻')
        ],
        [
            KeyboardButton('help us with money💳')
        ],
        [
            KeyboardButton('other bots with us🤖')
        ]
        
    ],
    resize_keyboard=True
)