#############################################
#discord.pyのフレームワークを使うばーじょん
#こっちをメインで開発中
#
#残課題：ダイス機能の拡充、ちゃんと配列で扱って合算値とか出せるようにしたい
#        エラーハンドリングちゃんとできるようにしたい
#
#############################################
import discord
from discord.ext import commands

#標準的なもろもろライブラリ
import os
import sys
import random
import datetime
#Redis接続用モジュール
import r

#環境変数取得
environment = os.environ.get("TOKEN")
#環境変数がない(=ローカル環境)なら
if environment is None:
    import env

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
    await bot.change_presence(activity=discord.Game(f"ねこはねこーとなくよ"))

@bot.command()
#/nekoで呼ばれた時の処理
async def neko(ctx):
    """ねこはねこーとなくよ"""
    await ctx.send('ねこー')

@bot.command()
#ダイスロール！
async def roll(ctx, dice : str):
    """ダイスを振るよ。XdYの形式で渡してね"""
#サンプルコードコピペ。str型で持ってるから配列にしたいなあ
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('ふぉーまっとがちがうよ!')
        return
    await ctx.send(dice + 'を振るよ！')
#ここまではコピペでいいはず
    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
#うごかない
#    def diceroll(dice_size):
#        print(dice_size + '個のダイスを振るよ！')
#        num = np.random.randinit(1, int(dice_size))
#        return num
#    def simple_dice(dice_size, dice_num):
#        dice_val = np.array([], dtype=np.int64)
#        print(dice_val)
#        for i in range(dice_num):
#            dice_val = np.append(dice_val, dice(dice_size))
#            print('for文のなか！'+ dice_val)
#        msg = str(np.sum(dice_val)) + '=' + srt(dice_val)
#        return msg
#    await ctx.send(simple_dice(limit, rolls))
    await ctx.send(result)
@bot.command()
#Redisにデータを登録するコマンド
async def add(ctx, key, val):
    """/add key url : DBに値を登録するよ"""
    result = conn.get(key)
    if result is None:
        await ctx.send(key + 'に' + val + ' を登録するよ')
        conn.set(key, val)
    else:
        await ctx.send('既に値が入ってるよ！')

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
environment = os.environ.get("TOKEN")
if environment is None:
    print('環境変数TOKENがないのでenv.pyのTOKENを見て実行します')
    #テスト用につなぐ時はTOKEN_TEST
    bot.run(env.TOKEN)
else:
    print('環境変数TOKENに値があるのでそのTOKENを見て実行します')
    bot.run(environment)
