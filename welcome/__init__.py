from .welcome import Welcome

async def setup(bot):
    cog = Welcome(bot=bot)
    await cog.crtoken()
    await cog.load_menu_module()
    bot.add_cog(cog)