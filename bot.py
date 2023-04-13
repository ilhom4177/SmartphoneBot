from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from main import (
    start,
    about,
)
import os


TOKEN = os.environ.get("TOKEN")

def main():
    # updater
    updater = Updater(token=TOKEN)
    # dispatcher
    dispatcher = updater.dispatcher
    # handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text('📝 About'), about))

    # start bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()