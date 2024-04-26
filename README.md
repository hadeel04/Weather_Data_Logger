# Weather Forecast Web Application

This is a Flask-based web application that fetches weather forecast data for a specified location using the OpenWeatherMap API.
The application displays the weather data for the next three days, including temperature, humidity, wind speed, and a brief description.
It also generates a bar chart visualizing the average temperatures for the next two days.

## Prerequisites

Before running the application, ensure that you have the following dependencies installed:

- Python 3.x
- Flask
- Pandas
- Requests
- Matplotlib

You can install the required packages using pip.

## Installation

1. Clone the repository:  https://github.com/hadeel04/Weather_Data_Logger
2. Navigate to the project directory : Weather_Data_Logger
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/) and replace the `api_key` variable in the `app.py` file with your API key.

## Usage

1. Run the Flask application: python app.py
   2. Open your web browser and visit `http://localhost:5000/`.

3. Enter a location in the provided form and click the "Submit" button.

4. The application will fetch and display the weather forecast data for the specified location, including a bar chart showing the average temperatures for the next two days.


 

