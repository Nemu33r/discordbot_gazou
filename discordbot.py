# インストールした discord.py を読み込む
import discord
# 自分のBotのアクセストークンをenv.pyにTOKEN = 'hoge'の形でかく
import env


# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} Usageを出したいなあ' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

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

    # 「/hoge」と発言したら「なんか」が返る処理
    if message.content == '/abiko':
        await message.channel.send('https://cdn.discordapp.com/attachments/726092371799965789/818824755704102982/image0.gif')

    # 「/hoge」と発言したら「なんか」が返る処理
    if message.content == '/lonkis':
        await message.channel.send('https://cdn.discordapp.com/attachments/726092371799965789/818824755704102982/image0.gif')

    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

# Botの起動とDiscordサーバーへの接続
client.run(env.TOKEN)
