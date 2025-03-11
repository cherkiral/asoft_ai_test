import redis
from rq import Queue
from rq.serializers import JSONSerializer

redis_conn = redis.Redis(host="redis", port=6379, decode_responses=False)
queue = Queue("message_queue", connection=redis_conn, serializer=JSONSerializer)