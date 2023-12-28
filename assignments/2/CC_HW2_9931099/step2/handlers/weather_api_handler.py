import requests
from handlers.model.weather import Weather



def get_city_temperature_data(API_KEY, city):
    url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"

    querystring = {"city": f"{city}"}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response is not None and response.status_code == 200:
        response = response.json()
        return Weather(response['min_temp'], response['max_temp'])
    else:
        raise Exception('Some unexpected error occured.')


