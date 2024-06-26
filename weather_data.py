import requests
import os
from datetime import datetime

user_api = "ec30b20c8b7c7fd8342c6a3e2086623a"
#location = input("Please Enter City Name: ")
location= "Kolkata"

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

if api_data['cod'] == 404:
    print("Invalid city fellow")
else:
    # Create variables to store and display data
    temp_city = api_data['main']['temp'] - 273.15
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed'] * 3.6  # Convert m/s to km/h
    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    print("-------------------------------------------------------------")
    print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
    print("-------------------------------------------------------------")

    print("Current temperature is: {:.2f} deg C".format(temp_city))
    print("Current weather desc  :", weather_desc)
    print("Current Humidity      :", hmdt, '%')
    print("Current wind speed    :", wind_spd, 'km/h')
