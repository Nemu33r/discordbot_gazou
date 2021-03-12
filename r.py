import redis
import os
#デバッガ用
#import pdb; pdb.set_trace()

#ローカル環境なら
import env

def connect():
    #環境変数に既にREDIS_URLがあるなら
    #print(os.environ.get('REDIS_URL'))
    #return redis.from_url(
    #    url=os.environ.get('REDIS_URL'), # 環境変数にあるURLを渡す
    #    decode_responses=True, # 日本語の文字化け対策のため必須
    #)

    #ローカル環境等で環境変数にREDIS_URLがないなら
    print('Redisに接続します')
    return redis.from_url(
        url=env.REDIS_URL,
        decode_responses=True,

    )
