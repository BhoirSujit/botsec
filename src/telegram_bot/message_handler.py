import re
from telegram import Update
from link_scanner import check_link

from telegram.ext import CallbackContext

#process message 
async def process_message(update: Update, context: CallbackContext):
    text = update.message.text

    #check if it is link or not
    url_regex = r"(https?:\/\/[^\s]+)"
    links = re.findall(url_regex, text)


    if links:
        for link in links:
            #check link 
            result = check_link(link)
            print(result)  
            await update.message.reply_text(result) 
         