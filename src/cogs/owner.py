from discord import Object
from discord.ext.commands import Bot, Cog, Context, command


class Owner(Cog):
    def __init__(self, bot: Bot) -> None:
        """
        Initializes Owner cog
        bot: Discord bot to initialize command on
        """

        self.bot = bot

    @command(name="sync")
    async def sync(self, ctx: Context) -> None:
        """
        syncs the bot's tree
        ctx: Context of discord message
        """

        for guild in self.bot.guilds:
            await self.bot.tree.sync(guild=Object(id=guild.id))

        await ctx.send("Finished syncing")


async def setup(bot: Bot) -> None:
    """
    Adds owner cog to bot
    bot: Discord bot
    """

    await bot.add_cog(Owner(bot=bot))
