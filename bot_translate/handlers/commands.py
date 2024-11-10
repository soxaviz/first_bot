from data.loader import bot
from database.db import add_user
from keyboards.reply import start_kb

# i18n


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    add_user(chat_id)
    bot.send_message(chat_id,
                     'Добро пожаловать в бот переводчик! Выберите действие ниже',
                     reply_markup=start_kb())

