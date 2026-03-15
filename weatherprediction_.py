import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_csv("weather_history.csv",
                 names=["date","city","temperature","humidity","condition"])

df["day_index"] = range(len(df))

X = df[["day_index"]]
y = df["temperature"]

model = LinearRegression()
model.fit(X, y)

future_day = np.array([[len(df) + 1]])

predicted_temp = model.predict(future_day)

print(" Predicted next temperature:", predicted_temp[0])