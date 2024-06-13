import requests

city = input("Enter City: ")
country = input("Enter Country (use 2-letter ISO code): ")
state = ""

if country.upper() == "US":
    state = input("Enter State (if applicable): ")

api_key = "84d49f27e68dd133ed760ed3498ad524"
location_query = city

if state:
    location_query += f",{state}"
location_query += f",{country}"

url = f"http://api.openweathermap.org/data/2.5/weather?q={location_query}&appid={api_key}&units=metric"

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']

    print(f'Location: {city}, {state if state else ""} {country}')
    print('Temperature:', temp, '°C')
    print('Wind:', wind)
    print('Pressure:', pressure)
    print('Humidity:', humidity)
    print('Description:', description)
else:
    print("Error:", data.get("message", "Unable to fetch data."))
