import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL='https://api.openweathermap.org/data/2.5/weather'
API_KEY = os.getenv("WEATHER_API_KEY")
city_name = os.getenv("CITY_NAME")

def get_weather_data(city_name):
    url = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=imperial"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        data_filtered = {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"]
        }
        return data_filtered
    else:
        print(f"Error: {response.status_code}")
        print("Please check your API key and city name.")
    

