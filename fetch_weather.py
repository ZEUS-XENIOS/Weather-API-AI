import requests
import pandas as pd
from datetime import datetime

API_KEY = "a1aed98b3eb3b4bc029ec813a672de81"
CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

temp = data["main"]["temp"]
humidity = data["main"]["humidity"]
weather = data["weather"][0]["main"]

record = {
    "date": datetime.now(),
    "city": CITY,
    "temperature": temp,
    "humidity": humidity,
    "condition": weather
}

df = pd.DataFrame([record])

df.to_csv("weather_history.csv", mode="a", header=False, index=False)

print("✅ Weather data saved:", record)
