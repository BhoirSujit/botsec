from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler
from message_handler import process_message
from command_handler import hello, help


#load variables
from config import TEL_BOT_TOKEN

#ensure the token is loaded
if not TEL_BOT_TOKEN:
    raise ValueError("❌ Telegram bot token is missing! Check your .env file.")
print("✅ Token loaded successfully!")



# Create bot application
app = ApplicationBuilder().token(TEL_BOT_TOKEN).build()

#handle commands
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))

#handle messages
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, process_message))

if __name__ == "__main__":
    print("🤖 Bot is running...")
    app.run_polling()
