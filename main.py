from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/weather")
def get_weather():
    city = request.args.get("city")
    country = request.args.get("country")
    weather_data = get_current_weather(city, country)

    return render_template(
        "weather.html",
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
    app.run(port=8000)
