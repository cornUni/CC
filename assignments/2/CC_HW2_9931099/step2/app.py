from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from handlers.redis_handler import RedisHandler
from handlers.weather_api_handler import get_city_temperature_data

load_dotenv()

EXPIRATION_TIME = os.getenv('EXPIRATION_TIME')
PORT = os.getenv('PORT')
CITY = os.getenv('CITY')
API_KEY = os.getenv('API_KEY')

redis_client = RedisHandler()

app = Flask(__name__)
CORS(app)


@app.route('/ping', methods=['GET'])
def pong():
    return 'pong', 200

@app.route('/api/weather/', methods=['GET'])
def get_temperature_info(city = CITY):
    cached_value = redis_client.redis_get(city)
    result = {}

    if cached_value is not None:
        result = cached_value
    else:
        try:
            weather_data = get_city_temperature_data(API_KEY, city)
        except Exception as e:
            return jsonify({'error': e.__str__()}), 401
        

        redis_client.redis_cache(city, EXPIRATION_TIME, weather_data.to_json())
        result = weather_data.to_json()
    
    return result, 200

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=PORT)
    args = parser.parse_args()
    port = args.port
    app.run(host='0.0.0.0', port=port)
