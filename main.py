import g4f
import telebot
from telebot import asyncio_helper
from telebot import apihelper
import re


def chatgpt4(content):
    response = g4f.ChatCompletion.create(
        model=g4f.models.default,
        messages=[{"role": "user", "content": content}],
        proxy="http://127.0.0.1:7890",# Proxy Port,you can del this row
        timeout=120, # in secs
    )
    return response

# Proxy port,IF you don't need this you can del the two rows
apihelper.proxy = {'http':'http://127.0.0.1:7890','https':'http://127.0.0.1:7890'}
asyncio_helper.proxy = 'http://127.0.0.1:7890'


BOT_TOKEN = "YOUR TOKEN HERE"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, chatgpt4(message))

bot.infinity_polling()

