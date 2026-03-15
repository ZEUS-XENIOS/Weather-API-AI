import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import requests
from datetime import datetime

st.title("🌦️ Live Weather Prediction Dashboard")

API_KEY = "a1aed98b3eb3b4bc029ec813a672de81"
CITY = "Bangalore"

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()

# SAFE API handling
if "main" in data:

    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["main"]

    new_row = {
        "timestamp": datetime.now(),
        "city": CITY,
        "temp": temp,
        "humidity": humidity,
        "condition": condition
    }

    df_live = pd.DataFrame([new_row])
    df_live.to_csv("weather_history.csv", mode="a", header=False, index=False)

else:
    st.error(f"API Error → {data}")

# LOAD DATASET
df = pd.read_csv("weather_history.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values("timestamp")
df = df.set_index("timestamp")

# LIMIT SIZE (important for cloud)
df = df.tail(100)

st.subheader("📊 Historical Weather Data")
st.dataframe(df)

st.subheader("🌡️ Temperature Trend")
st.line_chart(df["temp"])

# ML MODEL
df["day_index"] = range(len(df))

X = df[["day_index"]]
y = df["temp"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[len(df) + 1]])
prediction = model.predict(future_day)[0]

st.subheader("🔮 Predicted Next Temperature")
st.success(f"{prediction:.2f} °C")