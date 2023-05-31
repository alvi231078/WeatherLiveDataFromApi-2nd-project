import requests

API_KEY = '1dde54c2957d4d37523307d58056a272'

while True:
    city = input("enter a city: ")
    country = input("enter a country: ")
    COUNTRY = country
    CITY = city
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&APPID=1dde54c2957d4d37523307d58056a272'
    response = requests.get(URL)
    weatherData = response.json()

    if weatherData['cod'] == '404':
        print("City not found!")

    else:
        temperature_kelvinN = weatherData['main']['temp']
        temperature_celciusN = round(temperature_kelvinN - 273.15)

        temperature_kelvinF = weatherData['main']['feels_like']
        temperature_celciusF = round(temperature_kelvinF - 273.15)
        weatherDescription = weatherData['weather'][0]['description']
        print(
            f'This is Noraml temperature {temperature_celciusN}\u00B0C  but it feels like {temperature_celciusF}\u00B0C also weather is like {weatherDescription.capitalize()}')

