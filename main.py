import os
from dotenv import load_dotenv
from telebot import TeleBot
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'salam, {message.from_user.first_name}')


def message_handler(bot, update):
    bot.send_message(update.message.chat.id, update.message.text)
    print(update.message.text)

bot.polling(none_stop=True)

