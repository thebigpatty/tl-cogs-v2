from redbot.core import commands, bank
import discord

from .shoproles import SHOP_ROLES 

class Shopv2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.roles_for_sale = SHOP_ROLES 

    async def _buy_role(self, ctx, tier_name):
        tier_data = self.roles_for_sale[tier_name]
        role = ctx.guild.get_role(tier_data["id"])
        cost = tier_data["cost"]
        prereq = tier_data["requires"]

        if not role:
            await ctx.send("That role doesn’t exist on this server.")
            return

        role_display = role.name if role else tier_name.capitalize()

        # Already owns role
        if role in ctx.author.roles:
            await ctx.send(f"You already own {role_display}!")
            return

        # Check prerequisite
        if prereq:
            prereq_role_id = self.roles_for_sale[prereq]["id"]
            prereq_role = ctx.guild.get_role(prereq_role_id)
            prereq_display = prereq_role.name if prereq_role else prereq.capitalize()
            if prereq_role not in ctx.author.roles:
                await ctx.send(f"You must own {prereq_display} before buying {role_display}!")
                return

        user_balance = await bank.get_balance(ctx.author)
        if user_balance < cost:
            await ctx.send(f"You need **{cost:,} credits** but only have **{user_balance:,} credits**.")
            return

        try:
            await ctx.author.add_roles(role, reason=f"Purchased {role.name} role")
            await bank.withdraw_credits(ctx.author, cost)
            await ctx.send(f"You successfully purchased **{role_display}** for **{cost:,} credits!** 🎉")
        except discord.Forbidden:
            await ctx.send("I don’t have permission to assign that role. Please tell an admin.")
        except discord.HTTPException:
            await ctx.send("Something went wrong assigning the role. Check the logs for more info")

    @commands.command()
    async def buybronze(self, ctx):
        await self._buy_role(ctx, "bronze")

    @commands.command()
    async def buysilver(self, ctx):
        await self._buy_role(ctx, "silver")

    @commands.command()
    async def buygold(self, ctx):
        await self._buy_role(ctx, "gold")

    @commands.command()
    async def buyplatinum(self, ctx):
        await self._buy_role(ctx, "platinum")

    @commands.command()
    async def buyarcane(self, ctx):
        await self._buy_role(ctx, "arcane")

    @commands.command(name="shop")
    async def roleshop(self, ctx):
        embed = discord.Embed(
            title="🏆 Role Shop",
            description="Earn credits and climb the ranks! Each tier has a payday bonus.",
            color=discord.Color.gold()
        )

        for name, data in self.roles_for_sale.items():
            role = ctx.guild.get_role(data["role_id"])
            role_display = role.name if role else name.capitalize()
            cost = data["cost"]
            payday = data["payday"]
            prereq = data["requires"]

            prereq_text = f"Requires **{self.roles_for_sale[prereq]['color']}**" if prereq else "No prerequisite"

            embed.add_field(
                name=f"{role_display}",
                value=(
                    f"💰 **Cost:** {cost:,} credits\n"
                    f"💵 **Payday bonus:** {payday:,} credits\n"
                    f"📜 {prereq_text}\n"
                    f"▶️ Command: `!buy{name}`"
                ),
                inline=False
            )

        embed.set_footer(text="Buy higher tiers to unlock bigger paydays!")
        await ctx.send(embed=embed)
