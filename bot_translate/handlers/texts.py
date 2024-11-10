from data.loader import bot, translator
from keyboards.reply import lang_kb, continue_kb
from telebot.types import ReplyKeyboardRemove
from googletrans import LANGCODES
from .commands import start
from database.db import add_translation
from keyboards.inline import fav_button



@bot.message_handler(func=lambda msg: msg.text == 'Перевод')
def start_translation(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык, с которого хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_from)


def get_lang_from(message):
    print(message.text)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Выберите язык на который хотите сделать перевод',
                     reply_markup=lang_kb())
    bot.register_next_step_handler(message, get_lang_to, message.text)


# get_lang_to(message, s)
def get_lang_to(message, lang_from):
    print('lang_from', lang_from)
    print('lang_to', message.text)
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Напишите слово или текст для перевода',
                     reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(message, translate, lang_from, message.text)


def translate(message, lang_from, lang_to):
    code_from = LANGCODES.get(lang_from)  # ru, en, uz, ge
    code_to = LANGCODES.get(lang_to)
    chat_id = message.chat.id

    translated_text = translator.translate(message.text, dest=code_to, src=code_from).text
    _id = add_translation(message.text, translated_text, code_from, code_to, chat_id)
    bot.send_message(chat_id, f'<i>{translated_text}</i>', parse_mode='HTML', reply_markup=fav_button(_id))
    bot.send_message(chat_id, 'Продолжить???????', reply_markup=continue_kb())
    bot.register_next_step_handler(message, continue_translation, lang_from, lang_to)


def continue_translation(message, lang_from, lang_to):
    if message.text == 'Нет':
        start(message)
    elif message.text == 'Да':
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Напишите слово или текст для перевода',
                         reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, translate, lang_from, lang_to)