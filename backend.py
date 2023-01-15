import os
import requests


def get_data(place, forecast_days=1):
    key = os.getenv("OPENWEATHER_API_KEY")
    url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={place}&appid={key}"
    print(url)

    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    number_of_values = forecast_days * 24
    filtered_data = filtered_data[:number_of_values]

    if type_of_info == "Temperature":

    elif type_of_info == "Sky":


    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Marseille", forecast_days=4))
