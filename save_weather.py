import json


def save_weather_to_file(city, weather_data):
    filename = f"{city}_weather.json"
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(weather_data, file, ensure_ascii=False, indent=4)
    print(f"{city} için hava durumu bilgileri {filename} dosyasına kaydedildi.")
