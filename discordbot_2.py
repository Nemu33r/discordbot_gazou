#discord.pyのフレームワークを使うばーじょん
import discord
from discord.ext import commands

#標準的なもろもろライブラリ
import os
import sys
import random
import datetime

# 自分のBotのアクセストークンをenv.pyにTOKEN = 'hoge'の形でかく
import env
#Redis接続用モジュール
import r

#botコマンド構造体の定義
description = '''Discord.pyをつかったBotだよ
Bot commands frameworkのふれーむわーくをつかっているよ
つくりかけなのでわからないと応答しないよ
'''
bot = commands.Bot(command_prefix='/', description=description)

#Redis接続用のモジュールを定義
conn = r.connect()

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
    """ダイスを振るよ。XdYの形式で渡してね"""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('ふぉーまっとがちがうよ!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(dice + 'を振るよ！')
    await ctx.send(result)

@bot.command()
#Redisにデータを登録するコマンド
async def add(ctx, key, val):
    """/add key url : DBに値を登録するよ"""
    await ctx.send(key + 'に' + val + ' を登録するよ')
    conn.set(key, val)

@bot.command()
#Redisに登録されているKeyの一覧を取得するコマンド
async def lists(ctx):
    """ /lists : DBに入っているkeyの一覧を取得するよ """
    lists = conn.keys()
    await ctx.send('いまDBには以下の値が入っているよ')
    await ctx.send(lists)

@bot.command()
#Redisからデータを削除するコマンド
async def delete(ctx, key):
    """/delete key : DBから値を削除するよ"""
    await ctx.send(key + 'に保存した値を削除するよ')
    result = conn.get(key)
    if result is None:
        await ctx.send('存在しないよ！')
    await conn.delete(key)

@bot.command()
#Redisからデータを削除するコマンド
async def ref(ctx, key):
    """/ref key : DBから値を取得するよ"""
    await ctx.send(key + 'に保存した値を表示するよ')
    result = conn.get(key)
    if result is None:
        await ctx.send('存在しないよ！')
    await ctx.send(result)

@bot.event
async def on_command_error(exception: Exception, ctx: commands.Context):
    if isinstance(exception, commands.BadArgument):
        await cnt.send('たぶんふぉーまっとがちがうよ！つかいかたは/help を見てね！')

#ログインする
bot.run(env.TOKEN)
