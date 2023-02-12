import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def create(ctx):
    message = ctx.message
    embed = discord.Embed(
        title="創建",
        description="這是一個示例消息",
        color=discord.Color.blue()
    )
    embed.set_footer(text="這是底部文字")
    await ctx.send(embed=embed)

bot.run('TOKEN')