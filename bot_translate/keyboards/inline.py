from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

def fav_button(translation_id):
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton(text='dobavte text', callback_data='{salam}')
    )