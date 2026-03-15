import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Weather Prediction Dashboard")

df = pd.read_csv("weather_history.csv")

# convert timestamp column properly
df["timestamp"] = pd.to_datetime(df["timestamp"])

# sort by time
df = df.sort_values("timestamp")

# set time as index for graph
df = df.set_index("timestamp")

st.subheader("Historical Data")
st.dataframe(df)

st.subheader("Temperature Trend")
st.line_chart(df["temp"])

df["day_index"] = range(len(df))

X = df[["day_index"]]
y = df["temp"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[len(df) + 1]])
prediction = model.predict(future_day)[0]

st.subheader("Predicted Next Temperature")
st.success(f"{prediction:.2f} °C")