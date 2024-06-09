Import Libraries:

requests: To make HTTP requests to the weather API.
os: To access environment variables (like your API key).
datetime: To get the current date and time.
Get API Key and City Name:

user_api = os.getenv("api_key"): Fetches your API key from an environment variable.
location = input("Please Enter City Name: "): Asks the user to enter the city name for which they want the weather information.
Form the API URL and Make the Request:

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api: Constructs the URL for the API request using the city name and API key.
api_link = requests.get(complete_api_link): Makes the request to the API.
api_data = api_link.json(): Converts the API response from JSON format to a Python dictionary.
Check for Invalid City:

if api_data['cod'] == 404: Checks if the API returns a 404 status code, which means the city is not found.
print("Invalid city fellow"): Prints an error message if the city is invalid.
Extract and Display Weather Information (If the city is valid):

temp_city = api_data['main']['temp'] - 273.15: Extracts the temperature in Kelvin and converts it to Celsius.
weather_desc = api_data['weather'][0]['description']: Extracts a short description of the weather (e.g., clear sky, rain).
hmdt = api_data['main']['humidity']: Extracts the humidity percentage.
wind_spd = api_data['wind']['speed'] * 3.6: Extracts the wind speed in meters per second and converts it to kilometers per hour.
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p"): Gets the current date and time in a readable format.
Print Weather Information:

Prints the weather information in a formatted manner, including:
The city name and current date/time.
The current temperature in Celsius.
The weather description.
The humidity percentage.
The wind speed in kilometers per hour.