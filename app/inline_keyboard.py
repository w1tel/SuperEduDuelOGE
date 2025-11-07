from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_markup_test_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3

    markup.add(
        InlineKeyboardButton("Практика", callback_data="cb_practise"),
        InlineKeyboardButton("Режимы", callback_data="cb_modes"),
        InlineKeyboardButton("Турниры", callback_data="cb_tournament"),
    )

    return markup
