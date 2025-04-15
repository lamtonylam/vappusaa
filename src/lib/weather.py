import requests
from datetime import datetime

def get_weather():
    current_year = datetime.now().year
    weather_url = "https://api.open-meteo.com/v1/forecast?latitude=60.1582&longitude=24.9597&hourly=temperature_2m,precipitation_probability,precipitation&timezone=Europe%2FMoscow&forecast_days=16"
    weather_response = requests.get(weather_url)

    weather_data = weather_response.json()
    weather_time_list = weather_data["hourly"]["time"]
    temperature_list = weather_data["hourly"]["temperature_2m"]
    precipitation_probability_list = weather_data["hourly"]["precipitation_probability"]
    precipitation_list = weather_data["hourly"]["precipitation"]

    weather_dict = {
        time: {
            "temperature": temperature,
            "precipitation_probability": precipitation_probability,
            "precipitation": precipitation,
        }
        for time, temperature, precipitation_probability, precipitation in zip(
            weather_time_list, temperature_list, precipitation_probability_list, precipitation_list
        )
    }

    filtered_weather = {
        time: data
        for time, data in weather_dict.items()
        if time[:10] in {f"{current_year}-04-30", f"{current_year}-05-01"}
    }

    return filtered_weather