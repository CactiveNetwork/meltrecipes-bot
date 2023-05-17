from discord import Interaction
from discord.app_commands import CommandTree


def setup(tree: CommandTree) -> None:
    """
    Sets up a slash command
    tree: Discord bot CommandTree
    """

    @tree.command(
        name="help", description="Provides help about each command and who the bot is"
    )
    async def help(interaction: Interaction) -> None:
        await interaction.response.send_message("Melty Bot is still under progress! 😭")
