
import os
from flask import Flask, request, jsonify, render_template, send_from_directory
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/images/<Paasbaan>')
def download_file(Paasbaan):
    return send_from_directory(app.config['images'], Paasbaan)

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/result.html', methods=['POST'])
def predict():
    rfc = joblib.load('model/rf_model')
    print('model loaded')

    if request.method == 'POST':
        # Get form inputs
        address = request.form['Location']
        dt_string = request.form['timestamp']

        # Geocoding the location
        geolocator = Nominatim(user_agent="http")
        location = geolocator.geocode(address, timeout=None)

        if not location:
            return render_template('result.html', prediction="Invalid location provided.")

        lat = [location.latitude]
        lon = [location.longitude]

        latlong = pd.DataFrame({'latitude': lat, 'longitude': lon})
        latlong['timestamp'] = dt_string

        # Convert timestamp
        latlong['timestamp'] = pd.to_datetime(latlong['timestamp'], errors='coerce')

        if latlong['timestamp'].isnull().any():
            return render_template('result.html', prediction="Invalid timestamp format. Use DD/MM/YYYY HH:MM:SS")

        # Reorder columns to keep timestamp first
        cols = latlong.columns.tolist()
        cols = cols[-1:] + cols[:-1]
        data = latlong[cols]

        # Extract datetime features
        column_1 = data.iloc[:, 0]
        DT = pd.DataFrame({
            "year": column_1.dt.year,
            "month": column_1.dt.month,
            "day": column_1.dt.day,
            "hour": column_1.dt.hour,
            "dayofyear": column_1.dt.dayofyear,
            "week": column_1.dt.isocalendar().week,
            "dayofweek": column_1.dt.dayofweek,
            "weekday": column_1.dt.weekday,
            "quarter": column_1.dt.quarter,
        })

        data = data.drop('timestamp', axis=1)
        final = pd.concat([DT, data], axis=1)

        # Safely select required columns by name
        features = ['month', 'day', 'hour', 'dayofyear', 'dayofweek', 'latitude', 'longitude']
        try:
            X = final[features].values
        except KeyError:
            return render_template('result.html', prediction="Required input features are missing.")

        # Predict using the model
        my_prediction = rfc.predict(X)
        label = my_prediction[0]

        if label == 0:
                result = 'Predicted crime: Act 379 - Robbery'
        elif label == 1:
            result = 'Predicted crime: Act 13 - Gambling'
        elif label == 2:
            result = 'Predicted crime: Act 279 - Accident'
        elif label == 3:
            result = 'Predicted crime: Act 323 - Violence'
        elif label == 4:
            result = 'Predicted crime: Act 302 - Murder'
        elif label == 5:
            result = 'Predicted crime: Act 363 - Kidnapping'
        else:
                result = 'Place is safe — no crime expected at that timestamp.'

        return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
