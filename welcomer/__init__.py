from .welcomer import Welcomer

async def setup(bot):
    cog = Welcomer(bot=bot)
    await cog.crtoken()
    bot.add_cog(cog)
