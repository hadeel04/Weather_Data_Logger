
import requests
import pandas as pd
from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64

# Set up the Flask app
app = Flask(__name__)

# OpenWeatherMap API key
api_key = "f0c4410af0f025292cfee95a8f672a9e"


# Fetch and store weather data
def fetch_weather_data():
    weather_data = []
    location = request.form['location']
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather_data.append({
        'location': location,
        'temperature': data['main']['temp'],
        'humidity': [data['main']['humidity']],
        'wind_speed': [data['wind']['speed']],
        'description': data['weather'][0]['description']
    })
    return pd.DataFrame(weather_data)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch and process weather data
        weather_df = fetch_weather_data()
        # Generate a plot
        plt.figure(figsize=(8, 6))
        weather_df.plot(x='location', y='temperature', kind='bar')
        plt.title('Current Weather Temperatures')
        plt.xlabel('Location')
        plt.ylabel('Temperature (°C)')
        plot_buffer = io.BytesIO()
        plt.savefig(plot_buffer, format='png')
        plot_buffer.seek(0)
        plot_data = base64.b64encode(plot_buffer.getvalue()).decode('utf-8')

        return render_template('index.html', weather_data=weather_df.to_html(), plot_data=plot_data)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
