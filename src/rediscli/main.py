import os

import dotenv
import redis

dotenv.load_dotenv()

r = redis.StrictRedis(host='localhost', password=os.environ['REDIS_PASSWORD'], port=6379, db=0)
print(r.get(name="test").decode('utf-8'))


