import sqlite3


def save_to_db(city, weather, temperature, humidity, feels_like):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            weather TEXT,
            temperature REAL,
            humidity INTEGER,
            feels_like REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    cursor.execute("INSERT INTO weather (city, weather, temperature, humidity, feels_like) VALUES (?, ?, ?, ?, ?)",
                   (city, weather, temperature, humidity, feels_like))
    conn.commit()
    conn.close()
    print(f"{city} için hava durumu bilgileri veritabanına kaydedildi.")
