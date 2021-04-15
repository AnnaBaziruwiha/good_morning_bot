import os
import random

from dotenv import load_dotenv
from telebot import TeleBot, types

load_dotenv()


TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = TeleBot(TOKEN)

signs = ['Овен', 'Телец', 'Близнецы',
         'Рак', 'Лев', 'Дева', 'Весы',
         'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
first = [
    "Сегодня — идеальный день для новых начинаний.",
    "Оптимальный день для того, чтобы решиться на смелый поступок!",
    ("Будьте осторожны, сегодня звёзды могут повлиять" +
        " на ваше финансовое состояние."),
    ("Лучшее время для того, чтобы начать новые отношения" +
        " или разобраться со старыми."),
    "Плодотворный день для того, чтобы разобраться с накопившимися делами."
]
second = [
    "Но помните, что даже в этом случае нужно не забывать про",
    "Если поедете за город, заранее подумайте про",
    "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
    "Если у вас упадок сил, обратите внимание на",
    ("Помните, что мысли материальны," +
        " а значит вам в течение дня нужно постоянно думать про")
]
second_add = [
    "отношения с друзьями и близкими.",
    "работу и деловые вопросы, которые могут так некстати помешать планам.",
    "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
    "бытовые вопросы — особенно те, которые вы не доделали вчера.",
    "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."
]
third = [
    "Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
    ("Знайте, что успех благоволит только настойчивым," +
        " поэтому посвятите этот день воспитанию духа."),
    ("Даже если вы не сможете уменьшить влияние ретроградного Меркурия," +
        " то хотя бы доведите дела до конца."),
    ("Не нужно бояться одиноких встреч — сегодня то самое время," +
        " когда они значат многое."),
    ("Если встретите незнакомца на пути — проявите участие," +
        " и тогда эта встреча посулит вам приятные хлопоты.")
]


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
        for sign in signs:
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


# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    # Если нажали на одну из 12 кнопок — выводим гороскоп
    if call.data == "zodiac":
        # Формируем гороскоп
        msg = (
            random.choice(first) + ' ' +
            random.choice(second) + ' ' +
            random.choice(second_add) + ' ' +
            random.choice(third)
        )
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id, msg)


bot.polling()
