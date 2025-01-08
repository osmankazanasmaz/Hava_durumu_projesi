import matplotlib.pyplot as plt

def plot_combined_weather(city, forecast_data):
    temps = [item['main']['temp'] for item in forecast_data['list'][:5]]
    feels_like_temps = [item['main']['feels_like'] for item in forecast_data['list'][:5]]
    times = [item['dt_txt'] for item in forecast_data['list'][:5]]

    plt.plot(times, temps, label="Gerçek Sıcaklık", marker="o")
    plt.plot(times, feels_like_temps, label="Hissedilen Sıcaklık", linestyle="--", marker="x")
    plt.title(f"{city} için 5 günlük sıcaklık tahmini")
    plt.xlabel("Zaman")
    plt.ylabel("Sıcaklık (°C)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()
