import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("weather_history.csv",
                 names=["date","city","temperature","humidity","condition"])

df["date"] = pd.to_datetime(df["date"])

plt.plot(df["date"], df["temperature"])
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.show()