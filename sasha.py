# unwanted things?
import json
import time
# telegram inputs
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


with open("imp.json", 'r') as I_var:
    Token = json.load("Token")


with open("message.json", 'r') as VI_var:
    help_str = json.load("help_str")


updater = Updater(Token, use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")
    time.sleep(5)
    update.message.reply_text("yo!")


def help(update: Update, context: CallbackContext):
    update.message.reply_text(help_str)


def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("test@test.com (I am not\
        giving mine one for security reasons)")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("Youtube Link => 'Link'\
    https://www.youtube.com/")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("LinkedIn URL => \
        https://www.linkedin.com/")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" %
                              update.message.text)


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" %
                              update.message.text)


def ban_command(update: Update, context: CallbackContext):
    pass


def kick_command(update: Update, context: CallbackContext):
    pass


def books_guide(update: Update, context: CallbackContext):
    pass


def Aichatbot(update: Update, context: CallbackContext):
    pass


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
# Under work
# My commands
# updater.dispatcher.add_handler(MessageHandler('ban', ban_command))
# updater.dispatcher.add_handler(MessageHandler('kick', kick_command))

# Filters out unknown commands
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()
