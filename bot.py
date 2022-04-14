from lib2to3.pgen2 import token
from turtle import update
from urllib import request
from telegram.ext import Updater, CommandHandler
import requests

def start(update, context):

    update.message.reply_text('Hola')

def cry(update, context):

    url = 'https://api.waifu.pics/sfw/cry'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        update.message.reply_text(data.get('url'))

def kiss(update, context):
    url = 'https://api.waifu.pics/sfw/kiss'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        update.message.reply_text(data.get('url'))

if __name__ == '__main__':

    updater = Updater(token='ADD_YOUR_TOKEN',use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('cry', cry))
    dp.add_handler(CommandHandler('kiss', kiss))

    updater.start_polling()
    updater.idle()