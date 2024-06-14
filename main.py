import requests
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta, timezone

def show_country_codes():
    country_codes = {
        "Afghanistan": "AF", "Albania": "AL", "Algeria": "DZ", "Andorra": "AD",
        "Angola": "AO", "Antigua and Barbuda": "AG", "Argentina": "AR", "Armenia": "AM",
        "Australia": "AU", "Austria": "AT", "Azerbaijan": "AZ", "Bahamas": "BS",
        "Bahrain": "BH", "Bangladesh": "BD", "Barbados": "BB", "Belarus": "BY",
        "Belgium": "BE", "Belize": "BZ", "Benin": "BJ", "Bhutan": "BT",
        "Bolivia": "BO", "Bosnia and Herzegovina": "BA", "Botswana": "BW", "Brazil": "BR",
        "Brunei": "BN", "Bulgaria": "BG", "Burkina Faso": "BF", "Burundi": "BI",
        "Cabo Verde": "CV", "Cambodia": "KH", "Cameroon": "CM", "Canada": "CA",
        "Central African Republic": "CF", "Chad": "TD", "Chile": "CL", "China": "CN",
        "Colombia": "CO", "Comoros": "KM", "Congo": "CG", "Costa Rica": "CR",
        "Croatia": "HR", "Cuba": "CU", "Cyprus": "CY", "Czech Republic": "CZ",
        "Denmark": "DK", "Djibouti": "DJ", "Dominica": "DM", "Dominican Republic": "DO",
        "Ecuador": "EC", "Egypt": "EG", "El Salvador": "SV", "Equatorial Guinea": "GQ",
        "Eritrea": "ER", "Estonia": "EE", "Eswatini": "SZ", "Ethiopia": "ET",
        "Fiji": "FJ", "Finland": "FI", "France": "FR", "Gabon": "GA",
        "Gambia": "GM", "Georgia": "GE", "Germany": "DE", "Ghana": "GH",
        "Greece": "GR", "Grenada": "GD", "Guatemala": "GT", "Guinea": "GN",
        "Guinea-Bissau": "GW", "Guyana": "GY", "Haiti": "HT", "Honduras": "HN",
        "Hungary": "HU", "Iceland": "IS", "India": "IN", "Indonesia": "ID",
        "Iran": "IR", "Iraq": "IQ", "Ireland": "IE", "Israel": "IL",
        "Italy": "IT", "Jamaica": "JM", "Japan": "JP", "Jordan": "JO",
        "Kazakhstan": "KZ", "Kenya": "KE", "Kiribati": "KI", "Kuwait": "KW",
        "Kyrgyzstan": "KG", "Laos": "LA", "Latvia": "LV", "Lebanon": "LB",
        "Lesotho": "LS", "Liberia": "LR", "Libya": "LY", "Liechtenstein": "LI",
        "Lithuania": "LT", "Luxembourg": "LU", "Madagascar": "MG", "Malawi": "MW",
        "Malaysia": "MY", "Maldives": "MV", "Mali": "ML", "Malta": "MT",
        "Marshall Islands": "MH", "Mauritania": "MR", "Mauritius": "MU", "Mexico": "MX",
        "Micronesia": "FM", "Moldova": "MD", "Monaco": "MC", "Mongolia": "MN",
        "Montenegro": "ME", "Morocco": "MA", "Mozambique": "MZ", "Myanmar": "MM",
        "Namibia": "NA", "Nauru": "NR", "Nepal": "NP", "Netherlands": "NL",
        "New Zealand": "NZ", "Nicaragua": "NI", "Niger": "NE", "Nigeria": "NG",
        "North Korea": "KP", "North Macedonia": "MK", "Norway": "NO", "Oman": "OM",
        "Pakistan": "PK", "Palau": "PW", "Panama": "PA", "Papua New Guinea": "PG",
        "Paraguay": "PY", "Peru": "PE", "Philippines": "PH", "Poland": "PL",
        "Portugal": "PT", "Qatar": "QA", "Romania": "RO", "Russia": "RU",
        "Rwanda": "RW", "Saint Kitts and Nevis": "KN", "Saint Lucia": "LC", "Saint Vincent and the Grenadines": "VC",
        "Samoa": "WS", "San Marino": "SM", "Sao Tome and Principe": "ST", "Saudi Arabia": "SA",
        "Senegal": "SN", "Serbia": "RS", "Seychelles": "SC", "Sierra Leone": "SL",
        "Singapore": "SG", "Slovakia": "SK", "Slovenia": "SI", "Solomon Islands": "SB",
        "Somalia": "SO", "South Africa": "ZA", "South Korea": "KR", "South Sudan": "SS",
        "Spain": "ES", "Sri Lanka": "LK", "Sudan": "SD", "Suriname": "SR",
        "Sweden": "SE", "Switzerland": "CH", "Syria": "SY", "Taiwan": "TW",
        "Tajikistan": "TJ", "Tanzania": "TZ", "Thailand": "TH", "Timor-Leste": "TL",
        "Togo": "TG", "Tonga": "TO", "Trinidad and Tobago": "TT", "Tunisia": "TN",
        "Turkey": "TR", "Turkmenistan": "TM", "Tuvalu": "TV", "Uganda": "UG",
        "Ukraine": "UA", "United Arab Emirates": "AE", "United Kingdom": "GB", "United States": "US",
        "Uruguay": "UY", "Uzbekistan": "UZ", "Vanuatu": "VU", "Vatican City": "VA",
        "Venezuela": "VE", "Vietnam": "VN", "Yemen": "YE", "Zambia": "ZM", "Zimbabwe": "ZW"
    }

    message = "\n".join([f"{country}: {code}" for country, code in country_codes.items()])
    try:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        messagebox.showinfo("Country Codes", message)
    except tk.TclError:
        print("Unable to open a Tkinter window. Here are the country codes:")
        print(message)

def get_local_time(timezone_offset):
    utc_time = datetime.now(timezone.utc)
    local_time = utc_time + timedelta(seconds=timezone_offset)
    return local_time.strftime("%A, %d %B %Y, %I:%M %p")

def get_forecast_data(city, country, state, api_key):
    location_query = f"{city},{country}"
    if state:
        location_query = f"{city},{state},{country}"

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location_query}&appid={api_key}&units=metric"
    res = requests.get(url)
    data = res.json()

    if res.status_code == 200:
        forecast_data = []
        for forecast in data['list']:
            forecast_time = datetime.fromtimestamp(forecast['dt'], timezone.utc) + timedelta(seconds=data['city']['timezone'])
            temp = forecast['main']['temp']
            description = forecast['weather'][0]['description']
            wind = forecast['wind']['speed']
            humidity = forecast['main']['humidity']
            pressure = forecast['main']['pressure']
            forecast_data.append((forecast_time.strftime("%A, %d %B %Y, %I:%M %p"), temp, description, wind, humidity, pressure))
        return forecast_data
    else:
        return None

# Show the country codes popup or print them if Tkinter cannot open
show_country_codes()

city = input("Enter City: ")
country = input("Enter Country (use 2-letter ISO code): ").upper()
state = ""

if country == "US":
    state = input("Enter State (if applicable): ")

api_key = input("API key: ")

location_query = f"{city},{country}"

if state:
    location_query = f"{city},{state},{country}"

# Current weather data
url = f"http://api.openweathermap.org/data/2.5/weather?q={location_query}&appid={api_key}&units=metric"

res = requests.get(url)
data = res.json()

if res.status_code == 200:
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    timezone_offset = data['timezone']

    local_time = get_local_time(timezone_offset)

    print(f'Location: {city}, {state if state else ""} {country}')
    print(f'Local Time: {local_time}')
    print(f'Temperature: {temp} °C')
    print(f'Wind: {wind} m/s')
    print(f'Pressure: {pressure} hPa')
    print(f'Humidity: {humidity} %')
    print(f'Description: {description}')
else:
    print("Error:", data.get("message", "Unable to fetch data."))

# 5-day forecast data
forecast_data = get_forecast_data(city, country, state, api_key)
if forecast_data:
    print("\n5-day Forecast:")
    for forecast in forecast_data[:5*8:8]:  # 5 days, taking one forecast per day
        forecast_time, temp, description, wind, humidity, pressure = forecast
        print(f'Date & Time: {forecast_time}')
        print(f'Temperature: {temp} °C')
        print(f'Weather: {description}')
        print(f'Wind: {wind} m/s')
        print(f'Humidity: {humidity} %')
        print(f'Pressure: {pressure} hPa')
        print('---')
else:
    print("Unable to fetch forecast data.")
