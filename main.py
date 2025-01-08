from get_weather import get_weather
from get_forecast import get_forecast
from save_weather import save_weather_to_file
from plot_weather import plot_combined_weather

api_key = 'YOUR_IP_KEY'
city = input("Lütfen hava durumunu öğrenmek istediğiniz şehri giriniz: ")

# Anlık hava durumu verisi
current_data = get_weather(api_key, city)
if current_data:
    save_weather_to_file(city, current_data)

# 5 günlük tahmin verisi
forecast_data = get_forecast(api_key, city)
if forecast_data:
    plot_combined_weather(city, forecast_data)
else:
    print("Tahmin bilgileri alınamadığı için grafik çizilemedi.")
