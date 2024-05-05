from flask import Flask, render_template, request
from weather_data import WeatherData

# Set up the Flask app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        weather_data = WeatherData()
        weather_data.fetch_weather_data()
        weather_data.generate_plot()
        return render_template('index.html', weather_data=weather_data.data.to_html(), plot_data=weather_data.plot_data)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
