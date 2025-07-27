from .shop import Shopv2

async def setup(bot):
    await bot.add_cog(Shopv2(bot))