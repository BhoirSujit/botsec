from telegram import Update
from telegram.ext import  ContextTypes


# Command handler functions
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}!')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'abe {update.effective_user.first_name}, mai koi madat wadat nahi karane wala')

