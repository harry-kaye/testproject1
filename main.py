import requests

city = input("Enter City:")

api_key = "84d49f27e68dd133ed760ed3498ad524"
url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric".format(city, api_key)

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    country = data['sys']['country']
    state = ""

    # If the country is the USA, get state using the geocoding API
    if country == "US":
        geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{country}&appid={api_key}"
        geo_res = requests.get(geo_url)
        geo_data = geo_res.json()
        if geo_res.status_code == 200 and geo_data:
            state = geo_data[0].get('state', "")

    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    print('City:', city)
    if state:
        print('State:', state)
    print('Country:', country)
    print('Temperature:', temp, '°C')
    print('Wind:', wind)
    print('Pressure:', pressure)
    print('Humidity:', humidity)
    print('Description:', description)
else:
    print("Error:", data.get("message", "Unable to fetch data."))
