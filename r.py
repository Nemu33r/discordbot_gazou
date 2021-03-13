import redis
import os
#デバッガ用
#import pdb; pdb.set_trace()

#ローカル環境なら
import env

def connect():
    #環境変数に既にREDIS_URLがあるなら
    environment = os.environ.get("REDIS_URL")
    if environment is None:
        #ローカル環境等で環境変数にREDIS_URLがないなら
        print('環境変数にREDIS_URLがないのでenv.pyを見てRedisへ接続します')
        return redis.from_url(
            url=env.REDIS_URL,
            decode_responses=True,

            )
    else:
        print('環境変数REDIS_URLが存在するためそちらを使用してRedisに接続します')
        return redis.from_url(
            url=environment, # 環境変数にあるURLを渡す
            decode_responses=True, # 日本語の文字化け対策のため必須
        )
