#discord.pyのフレームワークを使うばーじょん
import discord
from discord.ext import commands

#標準的なもろもろライブラリ
import os
import random
import datetime

# 自分のBotのアクセストークンをenv.pyにTOKEN = 'hoge'の形でかく
import env
#Redis接続用モジュール


#botコマンド構造体の定義
description = '''Discord.pyをつかったBotだよ\n Bot commands frameworkのふれーむわーくをつかっているよ'''
bot = commands.Bot(command_prefix='/', description=description)

#起動時の処理
@bot.event
#起動したら標準出力に自分の情報を出す
async def on_ready():
    print(datetime.datetime.now())
    print('以下の情報でログインしたよ')
    print(bot.user.name)
    print(bot.user.id)
    print('------------------------')

@bot.command()
#テストコード
async def foo(ctx, arg):
    await ctx.send(arg)

@bot.command()
#/nekoで呼ばれた時の処理
async def neko(ctx):
    """ねこはねこーとなくよ"""
    await ctx.send('ねこー')

@bot.command()
#ダイスロール！
async def roll(ctx, dice : str):
    """ダイスを振るよ。XdYの形式で渡してね。"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('ふぉーまっとがちがうよ!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(dice + 'を振るよ！')
    await ctx.send(result)

#ログインする
bot.run(env.TOKEN)
