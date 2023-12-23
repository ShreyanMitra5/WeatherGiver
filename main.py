import requests

API_KEY = "b2a4225a44b466d22849b8cbf6a6cc8f"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round((data["main"]["temp"] - 273.15) * 1.8 + 32, 2)

    print("Weather: ", weather)
    print("Temperature: ", temperature, "Farenheit")
else:
    print("An error occured.")