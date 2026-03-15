import pandas as pd
import random
from datetime import datetime, timedelta

data = []

base_temp = 30

# generate last 72 hours weather
for i in range(72):
    date = datetime.now() - timedelta(hours=72-i)
    temp = base_temp + random.uniform(-3, 3)
    humidity = random.randint(35, 70)

    data.append([date, "Bangalore", round(temp,2), humidity, "Clear"])

df = pd.DataFrame(
    data,
    columns=["date", "city", "temperature", "humidity", "condition"]
)

df.to_csv("weather_data.csv", index=False)

print(" Realistic dataset generated")