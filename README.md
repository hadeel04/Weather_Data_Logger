
# Flask Weather Web Application

## Overview

This Flask web application fetches weather data from the OpenWeatherMap API, processes it, and displays it on a webpage. Users can input a location, and the application retrieves the weather forecast for the next three days, showing average temperature, humidity, wind speed, and a brief description of the weather conditions.


## Features

- Fetches weather data from the OpenWeatherMap API.
- Displays average temperature, humidity, wind speed, and weather description for the next two days.
- Generates a plot of average temperatures for the selected location.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Flask
- Pandas
- Matplotlib
- Requests

## Installation

1. Clone the repository:

 
   git clone https://github.com/hadeel04/Weather_Data_Logger.git
   

2. Navigate to the project directory:

   
   cd flask-weather-app
   

3. Install the required dependencies:

   
   pip install -r requirements.txt
   

## Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Open a web browser and go to `http://localhost:5000`.
3. Enter a location in the input field and click the "Submit" button.
4. View the weather forecast and the plot of average temperatures for the next three days.

## Configuration

Before running the application, make sure to replace the `api_key` variable in `weather_data.py` with your own OpenWeatherMap API key.

```python
self.api_key = "your_api_key"
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter any problems or have any suggestions for improvement.




