from telegram import (
    Update,
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
    # send message
    if result:
        update.message.reply_text(f'Hi {first_name}! Welcome to our bot!')
    else:
        update.message.reply_text(f'Hi {first_name}! Welcome back!')
