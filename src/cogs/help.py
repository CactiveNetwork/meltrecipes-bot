from discord.ext.commands import Bot, Cog, Context, command


class Help(Cog):
    def __init__(self, bot: Bot) -> None:
        """
        Initializes Help Command
        bot: Discord bot to initialize command on
        """

        self.bot = bot

    @command(name="help")
    async def help(self, ctx: Context) -> None:
        """
        responds with help message
        ctx: Context of discord message
        """

        await ctx.send("Melty Bot is still under progress! 😭")


async def setup(bot: Bot) -> None:
    """
    Adds Help cog to bot
    bot: Discord bot
    """

    await bot.add_cog(Help(bot=bot))
