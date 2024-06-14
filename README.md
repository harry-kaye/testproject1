**Weather Forecast Application**
This project is a weather forecast application that provides a 5-day weather forecast for a specified location using the OpenWeatherMap API. The application is built using Python and Streamlit*, allowing for interactive and web-based visualizations.
* to be implemented in a future build. 

**Features**
•	Real-time Weather Data: Fetches the current weather data including temperature, humidity, wind speed, and weather description.
•	5-Day Weather Forecast: Provides a detailed 5-day weather forecast with temperature, humidity, wind speed, and weather description for each day.
•	Interactive Graph: Displays an interactive graph showing temperature and humidity trends over the next 5 days.
•	Streamlit Web Interface*: User-friendly web interface for entering location details and displaying weather data.
* to be implemented in a future build. 

**Requirements**
•	Python 3.x
•	Requests
•	Pandas
•	Matplotlib
* Streamlit - to be implemented in a future build. 

**Installation**
1.	Clone the Repository:
bash
Copy code
git clone https://github.com/harry-kaye/testproject1.git

2.	Install Dependencies:
Copy code
pip install -r requirements.txt
3.	Get OpenWeatherMap API Key:
o	Sign up at OpenWeatherMap to get a free API key.

**Usage**
1.	Run the Application:
  arduino
  Copy code
  streamlit run app.py (not implemented yet)
2.	Enter Location Details:
o	Enter the city name.
o	Enter the 2-letter country code (ISO code).
o	If the country is the United States, enter the state code.
o	Enter your OpenWeatherMap API key.
3.	Fetch and Display Forecast:
o	Click the "Fetch Forecast" button to retrieve and display the 5-day weather forecast.
o	View the forecast data in a table and interact with the graph showing temperature and humidity trends.

**Project Structure**
•	app.py: Main application script containing the Streamlit interface and logic for fetching and displaying weather data.
•	README.md: Project documentation.
•	requirements.txt: List of required Python packages.
Libraries Used
•	Streamlit: For building the web interface.
•	Requests: For making API calls to OpenWeatherMap.
•	Pandas: For handling and manipulating data.
•	Matplotlib: For plotting the weather data.

**Example**
Here’s an example of how to enter the inputs and what you can expect from the application:
1.	Enter City: London
2.	Enter Country: GB
3.	API Key: your_api_key
After clicking the "Fetch Forecast" button, you will see the weather data for the next 5 days, including a graph of temperature and humidity.

**Contributing**
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contact**
For any questions or suggestions, please feel free to create an issue in this repository.
________________________________________
Enjoy using the Weather Forecast Application!
________________________________________

**Example Command to Run the Application (streamlit not functional yet – use main.py in the main directory)**
sh
Copy code
streamlit run app.py

**Sample Input**
•	City: New York
•	Country: US
•	State: NY
•	API Key: your_api_key

**Sample Output**
•	Current Weather:
o	Temperature: 25°C
o	Wind: 3.5 m/s
o	Pressure: 1013 hPa
o	Humidity: 60%
o	Description: clear sky
o	Local Time: Monday, 14 June 2024, 03:00 PM
•	5-Day Forecast: A table and graph showing temperature and humidity trends over the next 5 days.
________________________________________
By using this application, you can easily stay updated with the latest weather forecasts for your desired locations. 
