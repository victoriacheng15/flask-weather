from flask import Flask, render_template, request
from weather import get_current_weather

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run(port=8000)
