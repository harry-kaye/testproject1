def get_country_code(country_name):
    # Dictionary containing country codes for the corresponding country names
    country_codes = {
        "United States": "US",
        "United Kingdom": "GB",
        "France": "FR",
        "Japan": "JP",
        "Australia": "AU",
        "China": "CN",
        "Russia": "RU",
        "United Arab Emirates": "AE",
        "Brazil": "BR",
        "Canada": "CA"
    }

    # Return the country code based on the country name
    return country_codes.get(country_name, "Unknown")


def main():
    # Prompt the user to input a city name and country
    city_name = input("Enter the name of the city: ")
    country_name = input("Enter the name of the country: ")

    # Get the country code corresponding to the country name
    country_code = get_country_code(country_name)

    # Output the city name and country code
    print("City:", city_name)
    print("Country Code:", country_code)


if __name__ == "__main__":
    main()
