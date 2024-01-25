#!/usr/bin/env python
# coding: utf-8

##"MTE5ODU2MTEzMTMwMDY2MzM0Nw.GQ7DGV.IYy0FZiialRVV_vhY4k0ik3gvwPcwM_FHHRCSc"
import discord
from discord.ext import commands

# 創建機器人實例
bot = commands.Bot(command_prefix='')

# 定義指令
@bot.command(name='完美')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send('完 美 ! (◍•ᴗ•◍)')
@bot.command(name='月喵')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send('認真又可愛的貓')
@bot.command(name='差評')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send('差評( ˘•ω•˘ )')
# @bot.command(name='規則')
# async def say_perfect(ctx):
#     # chanel=bot.get_channel(1198561923957006420)
#     await ctx.send('愛月喵') 

@bot.command(name='結婚')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send('以後要跟我結婚的人我不需要婚戒 我有好吃的就好')        
@bot.command(name='社群')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send(":ballot_box_with_check:[ TWITCH  - 個人勢台灣Vtuber]\n https://www.twitch.tv/lunymeow_tw \n\n:ballot_box_with_check:[ YOUTUBE ]\n https://youtube.com/@LunyMeow\n\n:ballot_box_with_check:[ DISCORD ]\n https://discord.gg/z2ASb5UxfJ \n\n:ballot_box_with_check:[ INSTAGRAM ] \n https://www.instagram.com/lunymeow/\n\n:ballot_box_with_check:[ Twitter ] \n https://twitter.com/LunyMeow \n\n:ballot_box_with_check:[ Steam社群] \n https://steamcommunity.com/groups/lunymeow")  

@bot.command(name='!MOD', help='MOD們')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send("📢 本台MOD\n雪因, 大布丁超級大, 文隆, 白金金狗勾, 卡菈諾菈, Yaaa, 野豬騎士來嘍, GSEGWH, 阿阿阿阿宥, 呱呱")

@bot.command(name='!技術支援', help='月喵醬製造商')
async def say_perfect(ctx):
    # chanel=bot.get_channel(1198561923957006420)
    await ctx.send("若需增加任何指令請先詢問月喵後洽詢米納(Minazuki_Yi)")

# 設定機器人事件
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    game = discord.Game('各位好！我是月喵醬 認真學習中')
    await bot.change_presence(status=discord.Status.idle, activity=game)

# 啟動機器人
bot.run('MTE5ODU2MTEzMTMwMDY2MzM0Nw.GQ7DGV.IYy0FZiialRVV_vhY4k0ik3gvwPcwM_FHHRCSc')









