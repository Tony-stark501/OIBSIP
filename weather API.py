import requests
import json

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def display_weather(data):
    if "weather" in data :
        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        city = data["name"]
        country = data["sys"]["country"]

        print(f"Weather in {city}, {country}:")
        print(f"Description: {weather_desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
    else:
        print("City not found.")

if __name__ == "__main__":
    api_key = "c7fc8e63f672bc0bc246b185f5abe963"
    location = input("Enter city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)
