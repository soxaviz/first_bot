from telebot import TeleBot
import settings
from googletrans import Translator

bot = TeleBot(token=settings.BOT_TOKEN)
translator = Translator()

# команды
# текстовые
# колбэк
