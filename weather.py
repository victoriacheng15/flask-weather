from dotenv import load_dotenv
from pprint import pprint
import requests, os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_current_weather(city, country):
    URL = f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city},{country}&units=metric"
    weather_data = requests.get(URL).json()
    return weather_data
