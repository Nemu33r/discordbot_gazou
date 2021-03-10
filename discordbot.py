# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODE4ODM1Mzg4MjIyNzk5OTE0.YEd14Q.OfrOpMzOA77-XYwjwm1CgWInn3A'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    # 「/hoge」と発言したら「なんか」が返る処理
    if message.content == '/gaming_shoe':
        await message.channel.send('https://cdn.discordapp.com/attachments/819156022287532053/819156068046340136/image0.gif')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
