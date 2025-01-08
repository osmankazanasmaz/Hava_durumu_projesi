import requests
from save_to_db import save_to_db


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        feels_like = data['main']['feels_like']
        print(f"Hava Durumu: {weather}")
        print(f"Sıcaklık: {temperature}°C")
        print(f"Nem: %{humidity}")
        print(f"Hissedilen Sıcaklık: {feels_like}°C")
        save_to_db(city, weather, temperature, humidity, feels_like)
        return data
    elif response.status_code == 404:
        print(f"{city} adlı bir şehir bulunamadı. Lütfen doğru yazıldığından emin olun.")
        return None
    elif response.status_code == 401:
        print("API anahtarınız hatalı. Lütfen kontrol edin.")
        return None
    else:
        print("Hava durumu bilgileri alınamadı, lütfen şehir adını kontrol edin veya daha sonra tekrar deneyin.")
        return None
