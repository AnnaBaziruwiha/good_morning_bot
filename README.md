# Botstrology

:ringed_planet: Telegram bot that sends the horoscope for the day on request: it generates a forecast by combining four pieces of sentences. :ringed_planet:

## Technologies
- Python
- pytelegrambotapi

## Description
You start the bot with the **/start** command, the bot asks you whether you want today's horoscope, you should send **давай**, and choose your zodiac sign from the selection. The bot will then generate a random forecast and send it to you.

## Environment variables
The **horoscope_generator/handlers.py** uses the **TOKEN** variable - this is your bot's token, you can get it from the @BotFather bot right after your bot's registration. Keep it in a separate location.
## Bot's deployment

To deploy your own horoscope bot:
1. Clone the repository
2. Create a virtual environment in your project's directory
3. Run the virtual environment and install the requirements
4. Create an .env file in the horoscope_generator directory
5. Register a new Telegram bot using [@BotFather](https://t.me/BotFather)
6. Save your bot's token to the .env file
7. Run the bot

### Clone the repository
Run the following script in bash
```sh
git clone https://github.com/AnnaBaziruwiha/good_morning_bot.git
```

### Create virtual environment
Move to the project's directory **good_morning_bot**, and run the script
```sh
python3 -m venv venv
```

### Run the virtual environment and install the requirements
Run the virtual environment
```sh
source ./venv/scripts/activate # для windows
source ./venv/bin/activate # для linux
```

Install the requirements
```sh
(venv)
pip install -r requirements.txt
```

### Run the bot
Run the following script in the project's directory
```sh
python3 main.py
```

If you delploy your bot like that, it will only work while your computer is on and this script is running. If you need it to always be running, you can deploy it on a server.

### Contacts
Check out more of my projects [here](https://github.com/AnnaBaziruwiha)

You can send requests and suggestions [to this address](https://t.me/a_bzrwh)

My [linkedin](https://www.linkedin.com/in/annabaziruwiha/)
