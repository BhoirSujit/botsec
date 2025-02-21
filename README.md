# botsec

#setup

first clone our repository to your local machine
git clone https://github.com/BhoirSujit/botsec.git

after than you need to create ".env" file at root 
(open telegram and serach for "BotFather" and create new bot with /newbot command, name it and get your telegram bot token)

TEL_BOT_TOKEN=XXXXX(add your telegram bot api token)
SERVER_HOST=127.0.0.1 (change when you deploy it)
SERVER_PORT=8000 (change according your server)

run server with
py .\src\server\server.py

run bot server with
py .\src\telegram_bot\bot.py

finally add your bot to your group 
