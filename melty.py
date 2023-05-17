from config import config

from src.melty_bot import run

from dotenv import load_dotenv
from os import environ

from discord import Intents

load_dotenv(dotenv_path=config["env"]["path"])
token = environ["BOT_TOKEN"]

intents = Intents.all()

run(token=token, intents=intents)
