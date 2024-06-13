import requests

def get_coordinates(city_name, api_key):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    if data:  # Check if the list is not empty
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        return lat, lon
    else:
        print("City not found.")
        return None, None

def get_weather(lat, lon, api_key):
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    city_name = input("Enter the name of the city: ")
    api_key = "84d49f27e68dd133ed760ed3498ad524"  # Replace with your OpenWeather API key
    lat, lon = get_coordinates(city_name, api_key)
    if lat is not None and lon is not None:
        weather_data = get_weather(lat, lon, api_key)
        current_weather = weather_data["current"]
        print("Current Weather in", city_name)
        print("Temperature:", current_weather["temp"], "°C")
        print("Weather:", current_weather["weather"][0]["description"])
        print("Humidity:", current_weather["humidity"], "%")
        print("Wind Speed:", current_weather["wind_speed"], "m/s")
    else:
        print("Unable to retrieve weather data for the specified city.")

if __name__ == "__main__":
    main()
