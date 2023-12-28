import redis



class RedisHandler:
    def __init__(self) -> None:
        self.__redis_client = redis.Redis(host='redis', port=6379, db=0)

    def redis_get(self, city):
        return self.__redis_client.get(city)

    def redis_cache(self, city, expiration_time, weather_info) -> bool:
        if self.__redis_client.setex(city, expiration_time, weather_info) == 'OK':
            return True
        return False
