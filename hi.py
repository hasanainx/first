from telegram import *
from telegram.ext import *

bot = Bot("1659482970:AAGL_iItz_1JLqwXfH57kaqpGsF36L2KFNg")
updater = Updater("1659482970:AAGL_iItz_1JLqwXfH57kaqpGsF36L2KFNg")
dispatcher = updater.dispatcher


def test_function(update: Update,context: CallbackContext):
    bot.send_message(

        chat_id=update.effective_chat.id,
        text = "Hi"
    )
start_value=CommandHandler("Motion_detection", test_function)

dispatcher.add_handler(start_value)

updater.start_polling()

