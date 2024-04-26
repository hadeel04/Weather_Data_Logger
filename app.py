import requests
import pandas as pd
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
from datetime import datetime, timedelta

# Set up the Flask app
app = Flask(__name__)

# OpenWeatherMap API key
api_key = "f0c4410af0f025292cfee95a8f672a9e"

# Fetch and store weather data
def fetch_weather_data():
    weather_data = []
    location = request.form['location']
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    # Get the next 3 days' data
    dates = [datetime.fromtimestamp(data['list'][0]['dt']).date() + timedelta(days=d) for d in range(3)]

    for date in dates:
        day_data = [forecast for forecast in data['list'] if datetime.fromtimestamp(forecast['dt']).date() == date]
        avg_temp = sum(forecast['main']['temp'] for forecast in day_data) / len(day_data)
        avg_humidity = sum(forecast['main']['humidity'] for forecast in day_data) / len(day_data)
        avg_wind_speed = sum(forecast['wind']['speed'] for forecast in day_data) / len(day_data)

        weather_data.append({
            'location': location,
            'temperature': avg_temp,
            'humidity': avg_humidity,
            'wind_speed': avg_wind_speed,
            'description': day_data[0]['weather'][0]['description'],
            'date': date
        })

    return pd.DataFrame(weather_data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch and process weather data
        weather_df = fetch_weather_data()
        weather_df_day = (weather_df.loc[0]).to_frame()

        # Convert date column to datetime objects
        weather_df['date'] = pd.to_datetime(weather_df['date'])

        # Generate a plot
        plt.figure(figsize=(12, 6))
        plt.bar(weather_df['date'].dt.strftime('%Y-%m-%d'), weather_df['temperature'])
        plt.title('Average Weather Temperatures for the Next 2 Days')
        plt.xlabel('Date')
        plt.ylabel('Temperature (°C)')
        plt.xticks(rotation=45)
        plot_buffer = io.BytesIO()
        plt.savefig(plot_buffer, format='png', bbox_inches='tight')
        plot_buffer.seek(0)
        plot_data = base64.b64encode(plot_buffer.getvalue()).decode('utf-8')

        return render_template('index.html', weather_data=weather_df_day.to_html(), plot_data=plot_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)