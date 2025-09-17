import telebot
from dotenv import load_dotenv
import os
from telebot.types import Message
import json
from pathlib import Path
from typing import Any



load_dotenv()
TOKEN = os.getenv("TOKEN")
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
USERS_PATH = DATA_DIR / "users.json"
QUESTIONS_PATH = PROJECT_ROOT / "questions" / "bank.json"

bot = telebot.TeleBot(token=TOKEN)

def ensure_data() -> None:
    """Убедиться, что каталог data/ и users.json существуют.
    Если users.json нет — создаём пустой словарь пользователей.
    """
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not USERS_PATH.exists():
        USERS_PATH.touch()
        USERS_PATH.write_text("{}", encoding="utf-8")



def read_json(path: Path) -> Any:
    """Прочитать JSON из файла. Возвращает Python-объект."""
    text = path.read_text(encoding="utf-8")
    return json.loads(text) if text else {}

@bot.message_handler(commands=["start"])
def start_command(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Приветствуем в боте для подготовке к ОГЭ!')

@bot.message_handler(commands=["help"])
def help_command(message: Message):
    bot.send_message(chat_id=message.chat.id, text='Помощь зала блин')

if __name__ == "__main__":
    ensure_data()
    print("Bot is running…")
    bot.infinity_polling(skip_pending=True)