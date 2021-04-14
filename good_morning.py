import logging
import os
import random as r

from dotenv import load_dotenv
from pyrogram import Client

load_dotenv()


API_ID = os.getenv("api_id")
API_HASH = os.getenv("api_hash")
CHAT_ID = os.getenv("CHAT_ID")

greetings = ["Доброе утро", "Гуд морнинг", "Гутен морген",
             "Буенос Диас", "С утречком"]
cute_names = ["солнышко", "пупусик", "сладусик", "малышок",
              "пупсик", "солнце", "зайка"]

logging.basicConfig(level=logging.DEBUG)

r.seed()
greeting_number = r.randint(0, (len(greetings)-1))
cute_name_number = r.randint(0, (len(cute_names)-1))
message = f'{greetings[greeting_number]}, {cute_names[cute_name_number]}!'

with Client("my_account", api_id=API_ID, api_hash=API_HASH) as app:
    app.send_message(chat_id=CHAT_ID, text=message)
