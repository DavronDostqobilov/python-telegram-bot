import telegram
import time
import os
import pprint

TOKEN=os.environ['TOKEN']
bot = telegram.Bot(TOKEN)


last_update_id=-1

while True:
    update = bot.getUpdates()[-1]
    update_id = update.update_id
    chat_id = update.message.chat.id
    last_update=update.message
    print(last_update)
    
    if update_id != last_update_id:
        if  update.message.sticker:
            sticker=update.message.sticker.file_id
            bot.sendSticker(chat_id,sticker)
        elif update.message.photo:
            photo=update.message.photo[0]['file_id']
            bot.sendPhoto(chat_id, photo)
        elif update.message.text:
            text = update.message.text
            bot.sendMessage(chat_id, text)
        
        
        last_update_id = update_id
    time.sleep(2)
