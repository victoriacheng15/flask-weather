from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
from datetime import datetime

app = Flask(__name__)

def get_date_time():
    date = datetime.now().date().strftime('%Y-%m-%d')
    time = datetime.now().time().strftime("%H:%M")
    info = {"date": date, "time": time}
    return info


@app.route("/")
def index():
    info = get_date_time()
    return render_template("index.html", info=info)


@app.route("/weather")
def get_weather():
    info = get_date_time()
    city = request.args.get("city")
    country = request.args.get("country")
    weather_data = get_current_weather(city, country)

    return render_template(
        "weather.html",
        info=info,
        title=weather_data["name"],
        country=weather_data["sys"]["country"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        min_temp=f"{weather_data['main']['temp_min']:.1f}",
        max_temp=f"{weather_data['main']['temp_max']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        humidity=f"{weather_data['main']['humidity']}",
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
