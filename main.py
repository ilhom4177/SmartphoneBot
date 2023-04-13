from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from db import UserDb

userdb = UserDb()

def start(update: Update, context):
    '''Start command handler'''
    # get user info
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    last_name = update.message.chat.last_name
    username = update.message.chat.username
    # add user to db
    result = userdb.add_user(chat_id, first_name, username, last_name)
    # menu buttons
    keyboard = [
        [KeyboardButton('🛒 Buy'), KeyboardButton('📦 Order')],
        [KeyboardButton('📝 About'), KeyboardButton('📞 Contact')],
    ]
    # send message
    if result:
        update.message.reply_text(f'Hi {first_name}! Welcome to our bot!', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))
    else:
        update.message.reply_text(f'Hi {first_name}! Welcome back!', reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))


def about(update: Update, context):
    '''About command handler'''
    # send message
    update.message.reply_text('This is a bot for buying products from different companies.')