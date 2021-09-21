import os
try:
	from telegram.ext import Updater,CommandHandler
except:
	os.system("pip install python-telegram-bot")

def start(update,context):
	update.message.reply_text("Welcom")

updater = Updater(token='2039128835:AAHKF-6ONhf8d6cb1-6rcRxgdyFBDak3DIo',use_context=True)

updater.dispatcher.add_handler(CommandHandler("start",start))
updater.start_polling()
