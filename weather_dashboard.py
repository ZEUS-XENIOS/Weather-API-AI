import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

st.title("Weather Prediction Dashboard")
df = pd.read_csv("weather_data.csv")

# convert date column properly
df["date"] = pd.to_datetime(df["date"])

# sort by time
df = df.sort_values("date")

# set time as index for graph
df = df.set_index("date")

names=(["date","city","temperature","humidity","condition"])

st.subheader(" Historical Data")
st.dataframe(df)

st.subheader(" Temperature Trend")
st.line_chart(df["temperature"])

df["day_index"] = range(len(df))

X = df[["day_index"]]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[len(df)+1]])
prediction = model.predict(future_day)[0]

st.subheader(" Predicted Next Temperature")
st.success(f"{prediction:.2f} °C")