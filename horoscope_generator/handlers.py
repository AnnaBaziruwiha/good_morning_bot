import os
import random

from dotenv import load_dotenv
from telebot import TeleBot, types

from .data import (ADDITION_TO_SECOND_PART, FIRST_PART, SECOND_PART, SIGNS,
                   THIRD_PART)

load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, ("Хэй, как насчет гороскопа на сегодня?" +
                           " чтобы выбрать свой знак, отправь слово 'давай'"))


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "давай":
        bot.send_message(
            message.from_user.id,
            "Сейчас я расскажу тебе гороскоп на сегодня."
        )

        keyboard = types.InlineKeyboardMarkup()
        for sign in SIGNS:
            key = types.InlineKeyboardButton(text=sign, callback_data='zodiac')
            keyboard.add(key)

        bot.send_message(
            message.from_user.id,
            text='Выбери свой знак зодиака',
            reply_markup=keyboard
        )
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши давай")
    else:
        bot.send_message(
            message.from_user.id,
            "Я тебя не понимаю. Напиши /help."
        )


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    '''Обрабатывает нажатия кнопок'''
    if call.data == "zodiac":
        msg = (
            random.choice(FIRST_PART) + ' ' +
            random.choice(SECOND_PART) + ' ' +
            random.choice(ADDITION_TO_SECOND_PART) + ' ' +
            random.choice(THIRD_PART)
        )
        bot.send_message(call.message.chat.id, msg)
