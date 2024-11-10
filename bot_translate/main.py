from data.loader import bot

def main():
    from handlers import commands, texts, collbakcs


    print('bot working')
    bot.infinity_polling()

main()