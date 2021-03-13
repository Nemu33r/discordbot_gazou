# disrordbot_gazou  
Discordに接続して動くBotです。  
下記のことができます。  
・Key-Valueの紐付けをRedis(KVS)で保持  
→Discord上に上がったgifやスタンプなどの画像URLを保持、  
　参照された時に返す運用を想定しています  
・ダイスロール  

##注意点  
接続先のDBは一つなので、複数のサーバにおなじBotを入れると競合します。  
(複数のサーバに渡って同じ値を保持する)  
出し分け出来るようにはしたいですが、現状できません。  

##動作環境  
heroku + Heroku Redius add-in  
discord.py内のcommandsフレームワークを使っています。  
ローカルでも動作しますが、その場合はコードと同ディレクトリに  
TOKEN(bot接続用), REDIS_URL(REDIS接続用)を記述した  
env.pyを用意してください。  

##今後の課題  
・エラーハンドリング  
→想定外のparamを渡された時にwarnを上げるとか  
・機能拡充  
→ダイスのsumを出したい  
　→上ができたらXdY+AdB-Zみたいなある程度複雑な構文も理解できるようにしたい  
