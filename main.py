import requests
import tkinter as tk
from tkinter import messagebox

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
    messagebox.showinfo("Country Codes", message)

# Create a simple Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the main window

print("Use the 2 letter country code displayed here. Close the popup to continue.")
# Show the country codes popup
show_country_codes()

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
