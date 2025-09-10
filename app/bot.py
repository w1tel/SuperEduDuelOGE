import telebot
from dotenv import load_dotenv
import os
from telebot.types import Message

load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def start_command(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Приветствуем в боте для подготовке к ОГЭ!')

@bot.message_handler(commands=["help"])
def help_command(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Помощь зала блин')


if __name__ == "__main__":
    print("Bot is running…")
    bot.infinity_polling(skip_pending=True)