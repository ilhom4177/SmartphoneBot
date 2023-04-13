from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
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


def contact(update: Update, context):
    '''Contact command handler'''
    # inline keyboard
    inline_keyboard = [
        [   
            InlineKeyboardButton('📞Phone', callback_data='phone-number'), 
            InlineKeyboardButton('📧Email', callback_data='email-address')
        ],
        [
            InlineKeyboardButton('📍Location', callback_data='location'),
            InlineKeyboardButton('🎯Address', callback_data='address')
        ]
    ]

    # send message
    update.message.reply_text('Contact us:', reply_markup=InlineKeyboardMarkup(inline_keyboard))


def contact_callback(update: Update, context):
    '''Contact callback handler'''
    # inline keyboard
    inline_keyboard = [
        [   
            InlineKeyboardButton('📞Phone', callback_data='phone-number'), 
            InlineKeyboardButton('📧Email', callback_data='email-address')
        ],
        [
            InlineKeyboardButton('📍Location', callback_data='location'),
            InlineKeyboardButton('🎯Address', callback_data='address')
        ]
    ]
    # get callback data
    query = update.callback_query
    data = query.data
    # send message
    if data == 'phone-number':
        query.edit_message_text(text='Phone number: 998 90 123 45 67')