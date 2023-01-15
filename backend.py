import os
import requests


def get_data(place, forecast_days=1):
    key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={key}"

    response = requests.get(url)
    data = response.json()

    try:
        filtered_data = data["list"]
        number_of_values = forecast_days * 8
        filtered_data = filtered_data[:number_of_values]
    except KeyError:
        filtered_data = "ERROR"

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Marseille", forecast_days=4))
