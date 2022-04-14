from lib2to3.pgen2 import token
from turtle import update
from urllib import request, response
from telegram.ext import Updater, CommandHandler
import requests

def req(type,category):
    url = 'https://api.waifu.pics/'+type+'/'+category
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data.get('url') 

if __name__ == '__main__':

    updater = Updater(token='5160987677:AAHnMlG0MTieENZUvzJozrlCAZVLvEGpZtg',use_context=True)

    dp = updater.dispatcher
    
    #Type = SFW
    dp.add_handler(CommandHandler('waifu', lambda update,context: update.message.reply_text(req('sfw','waifu'))))
    dp.add_handler(CommandHandler('neko', lambda update, context: update.message.reply_text(req('sfw','neko'))))
    dp.add_handler(CommandHandler('shinobu', lambda update, context: update.message.reply_text(req('sfw','shinobu'))))
    dp.add_handler(CommandHandler('megumin', lambda update, context: update.message.reply_text(req('sfw','megumin'))))
    dp.add_handler(CommandHandler('bully', lambda update, context: update.message.reply_text(req('sfw','bully'))))
    dp.add_handler(CommandHandler('cuddle', lambda update, context: update.message.reply_text(req('sfw','cuddle'))))
    dp.add_handler(CommandHandler('cry', lambda update,context: update.message.reply_text(req('sfw','cry'))))
    dp.add_handler(CommandHandler('hug', lambda update, context: update.message.reply_text(req('sfw','hug'))))
    dp.add_handler(CommandHandler('awoo', lambda update, context: update.message.reply_text(req('sfw','awoo'))))
    dp.add_handler(CommandHandler('kiss', lambda update, context: update.message.reply_text(req('sfw','kiss'))))
    dp.add_handler(CommandHandler('lick', lambda update, context: update.message.reply_text(req('sfw','lick'))))
    dp.add_handler(CommandHandler('pat', lambda update, context: update.message.reply_text(req('sfw','pat'))))
    dp.add_handler(CommandHandler('smug', lambda update, context: update.message.reply_text(req('sfw','smug'))))
    dp.add_handler(CommandHandler('bonk', lambda update,context: update.message.reply_text(req('sfw','bonk'))))
    dp.add_handler(CommandHandler('yeet', lambda update, context: update.message.reply_text(req('sfw','yeet'))))
    dp.add_handler(CommandHandler('blush', lambda update, context: update.message.reply_text(req('sfw','blush'))))
    dp.add_handler(CommandHandler('smile', lambda update, context: update.message.reply_text(req('sfw','smile'))))
    dp.add_handler(CommandHandler('wave', lambda update, context: update.message.reply_text(req('sfw','wave'))))
    dp.add_handler(CommandHandler('highfive', lambda update, context: update.message.reply_text(req('sfw','highfive'))))
    dp.add_handler(CommandHandler('handhold', lambda update, context: update.message.reply_text(req('sfw','handhold'))))
    dp.add_handler(CommandHandler('nom', lambda update, context: update.message.reply_text(req('sfw','nom'))))
    dp.add_handler(CommandHandler('bite', lambda update, context: update.message.reply_text(req('sfw','bite'))))
    dp.add_handler(CommandHandler('glomp', lambda update, context: update.message.reply_text(req('sfw','glomp'))))
    dp.add_handler(CommandHandler('slap', lambda update, context: update.message.reply_text(req('sfw','slap'))))
    dp.add_handler(CommandHandler('kill', lambda update, context: update.message.reply_text(req('sfw','kill'))))
    dp.add_handler(CommandHandler('kick', lambda update, context: update.message.reply_text(req('sfw','kick'))))
    dp.add_handler(CommandHandler('happy', lambda update, context: update.message.reply_text(req('sfw','happy'))))
    dp.add_handler(CommandHandler('wink', lambda update, context: update.message.reply_text(req('sfw','wink'))))
    dp.add_handler(CommandHandler('poke', lambda update, context: update.message.reply_text(req('sfw','poke'))))
    dp.add_handler(CommandHandler('dance', lambda update, context: update.message.reply_text(req('sfw','dance'))))
    dp.add_handler(CommandHandler('cringe', lambda update, context: update.message.reply_text(req('sfw','cringe'))))
    ##Type = NSFW
    dp.add_handler(CommandHandler('hentai', lambda update, context: update.message.reply_text(req('nsfw','waifu'))))
    dp.add_handler(CommandHandler('furro', lambda update, context: update.message.reply_text(req('nsfw','neko'))))
    dp.add_handler(CommandHandler('trap', lambda update, context: update.message.reply_text(req('nsfw','trap'))))
    dp.add_handler(CommandHandler('blowjob', lambda update, context: update.message.reply_text(req('nsfw','blowjob'))))


    updater.start_polling()
    updater.idle()