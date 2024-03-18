# Flask Weather App

The Flask Weather App is a simple web application built with Flask, a lightweight Python web framework, designed to provide users with current weather information for any city worldwide. Leveraging the OpenWeather API, this app offers real-time weather data including temperature, humidity, wind speed, and weather description for the specified location.

[Live Site](https://flask-weather-vx15.onrender.com/)

> Please note that I'm using the free render plan, which means the website may take longer to spin up.

## How to run the App:

1. Clone the repository
```bash
git clone git@github.com:victoriacheng15/flask-weather.git

cd flask-weather
```
2. Install 
```bash
pip install -r requirements.txt
```
3. Obtain API Key
Sign up for an account on [OpenWeather](https://openweathermap.org/) to obtain an API key, which is required to access weather data.
4. Set Environment Variable
create `.env` file
```bash
WEATHER_API_KEY="YOUR_KEY"
```
5. Run the app
```bash
python3 main.py
```

## What have I learned?

In this project, I learned to define routes in Flask, facilitating URL endpoints for user interaction. Using `@app.route()`, I set up routes for the home and weather pages, dictating how the application responds to client reques

Example:
```py
# For home page
@app.route("/")

# For weather page
@app.route("/weather")
```

Additionally, I explored passing data between Python functions and HTML templates in Flask. By utilizing `render_template()`, I dynamically generated HTML content by transferring data from Python to templates. This allowed for the presentation of real-time weather information obtained from the OpenWeather API.

Example:
```py
# Pass data object with date and time properties to the home page
render_template("index.html", data={"date": date, "time": time})
```
```html
<!-- home page -->
<p class="date">Date: {{ data.date }}</p>
<p class="date">Current Time: {{ data.time }}</p>
```
```py
# Pass data as as individual property for weather page
render_template(
        "weather.html",
        title=weather_data["name"],
        country=weather_data["sys"]["country"],
        status=weather_data["weather"][0]["description"].capitalize(),
        # .... more
    )
```
```html
<!-- Weather page -->
<h2>{{ title }}, {{ country }} Weather</h2>
<p>Current Weather Status: {{ status }}</p>
<p>Tempature: {{ temp }}c&deg;</p>
```