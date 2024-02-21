import requests
import sys

def get_weather_data(location, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={location}"
    response = requests.get(complete_url)
    return response.json()

def display_weather_data(weather_data):
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"] - 273.15  # Convert from Kelvin to Celsius
        humidity = main_data["humidity"]

        weather_desc = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature:.1f}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_desc.capitalize()}")
    else:
        print("Location not found.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python weather_app.py <location> <api_key>")
        sys.exit(1)

    location = sys.argv[1]
    api_key = sys.argv[2]

    weather_data = get_weather_data(location, api_key)
    display_weather_data(weather_data)

    
    