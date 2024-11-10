from data.loader import bot

@bot.callback_query_handler(func=lambda call: call.data.startswith('fav'))
def add(callback):
    data = callback.data

    print(data)


    bot.answer_callback_query(callback.id, 'dobavleno')