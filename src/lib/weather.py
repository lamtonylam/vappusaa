from datetime import datetime
import requests_cache

session = requests_cache.install_cache(
    "weather_cache", expire_after=60
)  # Cache for 1 minute

import requests
from datetime import datetime


def fetch_weather_response(latitude=60.1582, longitude=24.9597):
    weather_url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m,precipitation_probability,precipitation"
        "&timezone=Europe%2FMoscow&forecast_days=16"
    )
    weather_response = requests.get(weather_url)
    return weather_response


def get_weather(latitude=60.1582, longitude=24.9597):
    weather_response = fetch_weather_response(latitude, longitude)
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
            weather_time_list,
            temperature_list,
            precipitation_probability_list,
            precipitation_list,
        )
    }

    return weather_dict


def get_filtered_weather_for_mayday(latitude=60.1582, longitude=24.9597):
    current_year = datetime.now().year
    weather_dict = get_weather(latitude, longitude)

    filtered_weather = {
        time: data
        for time, data in weather_dict.items()
        if time[:10] in {f"{current_year}-04-30", f"{current_year}-05-01"}
    }

    return filtered_weather


def check_if_date_is_in_weather_data(date_str, latitude=60.1582, longitude=24.9597):
    weather_dict = get_weather(latitude, longitude)

    for time in weather_dict.keys():
        if time[:10] == date_str:
            return True

    return False


def will_it_rain(date_str, latitude=60.1582, longitude=24.9597):
    weather_dict = get_weather(latitude, longitude)

    will_it_rain = False

    # Check if the date is in the weather data
    if not check_if_date_is_in_weather_data(date_str, latitude, longitude):
        return None

    for time, data in weather_dict.items():
        if time[:10] == date_str:
            if data["precipitation"] > 0:
                will_it_rain = True
                break

    return will_it_rain


def when_will_it_rain(date_str, latitude=60.1582, longitude=24.9597):
    weather_dict = get_weather(latitude, longitude)
    rain_data = []

    # Check if the date is in the weather data
    if not check_if_date_is_in_weather_data(date_str, latitude, longitude):
        return None

    for time, data in weather_dict.items():
        if time[:10] == date_str and data["precipitation"] > 0:
            rain_data.append({
                "time": datetime.fromisoformat(time).time(),
                "precipitation": data["precipitation"]
            })

    return rain_data
