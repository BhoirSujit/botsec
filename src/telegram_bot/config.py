import os
from dotenv import load_dotenv

load_dotenv()

TEL_BOT_TOKEN = os.getenv('TEL_BOT_TOKEN')
SERVER_HOST = os.getenv("SERVER_HOST")
SERVER_PORT = os.getenv("SERVER_PORT")