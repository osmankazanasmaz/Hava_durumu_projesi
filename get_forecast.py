import requests


def get_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 404:
        print(f"{city} adlı bir şehir bulunamadı. Lütfen doğru yazıldığından emin olun.")
        return None
    elif response.status_code == 401:
        print("API anahtarınız hatalı. Lütfen kontrol edin.")
        return None
    else:
        print("Hava durumu tahmini alınamadı, lütfen şehir adını kontrol edin veya daha sonra tekrar deneyin.")
        return None
