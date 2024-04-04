from dotenv import load_dotenv
import requests, os

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")


def get_current_weather(city, country):
    API_URL = "http://api.openweathermap.org/data/2.5/weather"
    URL = f"{API_URL}?appid={API_KEY}&q={city},{country}&units=metric"
    
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()