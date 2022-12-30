import requests



# Replace YOUR_API_KEY with your actual API key
API_KEY = 'YOUR_API_KEY'


# Set the city for which you want to get the weather
query = 'copenhagen'


try:
    response = requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={API_KEY}&q={query}')
    response.raise_for_status()
    data = response.json()
    city = data[0]['Key']
    name = data[0]['LocalizedName']
except requests.exceptions.HTTPError as err:
    print(err)



# Set the units to be used for temperature (either 'Imperial' or 'Metric')
units = 'Metric'

# Set the URL for the AccuWeather API
url = f'http://dataservice.accuweather.com/currentconditions/v1/{city}?apikey={API_KEY}&details=true'


# Make the API request
response = requests.get(url)


# Check for a successful request
if response.status_code == 200:
    # Get the data from the response
    data = response.json()
    # Get the current temperature in degrees Fahrenheit
    temperature = data[0]['Temperature'][units]['Value']
    unit_temperature = data[0]['Temperature'][units]['Unit']
    # Get the current weather condition
    condition = data[0]['WeatherText']
    # Get the current humidity
    humidity = data[0]['RelativeHumidity']
    # Get the current wind speed
    wind_speed = data[0]['Wind']['Speed'][units]['Value']
    unit_wind = data[0]['Wind']['Speed'][units]['Unit']
    # Print a summary of the current weather conditions
    
    
    print(f'The current temperature in {name} is {temperature}°{unit_temperature} with {condition.lower()} conditions and a humidity of {humidity}%. The wind is blowing at {wind_speed} {unit_wind}.')
else:
    # Print an error message if the request was unsuccessful
    print('An error occurred while trying to retrieve the weather data.')
