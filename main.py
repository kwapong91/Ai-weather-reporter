from utils import get_weather_data, city_name
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

weather = get_weather_data(city_name)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {"role": "system", "content": "You are a funny weather reporter. But you keep things short and simple."},
        {"role": "user", "content": f"Generate a short weather report for {city_name}. It's {weather['temperature']}°F. The weather is {weather['weather']}. Please make it funny and add a joke."},
    ]
)

print(completion.choices[0].message.content)
