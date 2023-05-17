from .file_utils import get_all_files

from config import config

from os.path import join
from importlib import import_module
import asyncio

from discord import Intents
from discord.ext.commands import Bot


def run(token: str, intents: Intents) -> None:
    """
    Runs Melty Bot
    token: Discord bot token
    intents: Discord bot intents
    """

    bot_id = config["bot"]["id"]
    client = Bot(command_prefix=f"<@{bot_id}> ", intents=intents, help_command=None)

    @client.event
    async def on_ready():
        print(f"Logged in successfully as {client.user}")

    cog_files = get_all_files(config["bot"]["cogs"]["path"], ".py")
    slash_command_files = get_all_files(config["bot"]["slash-commands"]["path"], ".py")

    for cog in cog_files:
        asyncio.run(
            client.load_extension(
                join(config["bot"]["cogs"]["path"], cog)
                .replace("./", "")
                .replace("/", ".")[:-3]
            )
        )
        print(
            "Cog initialized: "
            + join(config["bot"]["cogs"]["path"], cog)
            .replace("./", "")
            .replace("/", ".")[:-3]
        )

    for slash_command in slash_command_files:
        module = import_module(
            join(config["bot"]["slash-commands"]["path"], slash_command)
            .replace("./", "")
            .replace("/", ".")[:-3]
        )
        module.setup(tree=client.tree)
        print(
            "Slash Command initialized: "
            + join(config["bot"]["slash-commands"]["path"], slash_command)
            .replace("./", "")
            .replace("/", ".")[:-3]
        )

    client.run(token=token)
