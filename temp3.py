import requests
import streamlit as st
from datetime import datetime
import pytz


def get_country_codes():
    return {
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


def fetch_weather(city, country, state="", api_key="84d49f27e68dd133ed760ed3498ad524"):
    location_query = f"{city},{country}"
    if state:
        location_query = f"{city},{state},{country}"

    url = f"http://api.openweathermap.org/data/2.5/weather?q={location_query}&appid={api_key}&units=metric"
    res = requests.get(url)
    return res.json(), res.status_code


def get_local_time(timezone):
    local_time = datetime.now(pytz.timezone(timezone))
    return local_time.strftime("%A, %d %B %Y, %I:%M %p")


st.title("Weather Information")

country_codes = get_country_codes()

if st.button("Show Country Codes"):
    country_code_str = "\n".join([f"{country}: {code}" for country, code in country_codes.items()])
    st.text_area("Country Codes", value=country_code_str, height=200)

city = st.text_input("Enter City")
country = st.text_input("Enter Country (use 2-letter ISO code)").upper()
state = ""
if country == "US":
    state = st.text_input("Enter State (if applicable)")

if st.button("Get Weather Information"):
    data, status_code = fetch_weather(city, country, state)

    if status_code == 200:
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        timezone = data['timezone']

        local_time = get_local_time(
            pytz.timezone('UTC').localize(datetime.utcnow()).astimezone(pytz.timezone('Etc/GMT+0')).tzname())

        st.write(f"**Location:** {city}, {state if state else ''} {country}")
        st.write(f"**Local Time:** {local_time}")
        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Wind:** {wind} m/s")
        st.write(f"**Pressure:** {pressure} hPa")
        st.write(f"**Humidity:** {humidity} %")
        st.write(f"**Description:** {description}")
    else:
        st.write(f"Error: {data.get('message', 'Unable to fetch data.')}")
