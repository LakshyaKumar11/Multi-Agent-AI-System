import os
import requests
from dotenv import load_dotenv

# Load .env file from root
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

class WeatherCheckAgent:
    def get_weather(self, launch_info):
        key = os.getenv("OPEN_WEATHER_API_KEY")
        print("🔑 Loaded API KEY from .env:", key)  # DEBUG

        lat, lon = 28.5618571, -80.577366
        if not key:
            return {"error": "Missing OpenWeatherMap API key"}

        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}&units=metric"
        res = requests.get(url).json()
        print("🌦️ Weather API Response:", res)

        if "weather" not in res or "wind" not in res:
            return {"error": "Weather data not available", "response": res}

        return {
            "weather": res["weather"][0]["main"],
            "description": res["weather"][0]["description"],
            "wind_speed": res["wind"]["speed"]
        }
