# from flask import Flask, jsonify
# import pandas as pd
# import numpy as np
# from sklearn.linear_model import LinearRegression
# import csv
# from datetime import datetime

# app = Flask(__name__)
# def save_weather_row(city, temp, humidity, condition):
#     with open("weather_history.csv", "a", newline="") as f:
#         writer = csv.writer(f)
#         writer.writerow([datetime.now(), city, temp, humidity, condition])

# @app.route("/predict")
# def predict():

#     df = pd.read_csv("weather_history.csv",
#                      names=["date","city","temperature","humidity","condition"])

#     df["day_index"] = range(len(df))

#     X = df[["day_index"]]
#     y = df["temperature"]

#     model = LinearRegression()
#     model.fit(X, y)

#     future_day = np.array([[len(df) + 1]])
#     predicted_temp = model.predict(future_day)[0]

#     return jsonify({"predicted_temperature": float(predicted_temp)})

# app.run(debug=True)
from flask import Flask, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import csv
from datetime import datetime

app = Flask(__name__)

def save_weather_row(city, temp, humidity, condition):
    with open("weather_history.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), city, temp, humidity, condition])

@app.route("/predict")
def predict():

    # load dataset
    df = pd.read_csv(
        "weather_history.csv",
        names=["date","city","temperature","humidity","condition"]
    )

    # ⭐ simulate LIVE weather fetch (temporary logic)
    city = "Bangalore"
    live_temp = df["temperature"].iloc[-1] + np.random.uniform(-1, 1)
    humidity = np.random.randint(35, 70)
    condition = "Clear"

    # ⭐ save new row to CSV
    save_weather_row(city, round(live_temp,2), humidity, condition)

    # ⭐ reload updated dataset
    df = pd.read_csv(
        "weather_history.csv",
        names=["date","city","temperature","humidity","condition"]
    )

    # ML training
    df["day_index"] = range(len(df))

    X = df[["day_index"]]
    y = df["temperature"]

    model = LinearRegression()
    model.fit(X, y)

    future_day = np.array([[len(df) + 1]])
    predicted_temp = model.predict(future_day)[0]

    return jsonify({"predicted_temperature": float(predicted_temp)})

app.run(debug=True)
