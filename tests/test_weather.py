import pytest
import requests
import unittest.mock as mock
import weather


@mock.patch("requests.get")
def test_weather(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "name": "Test City",
        "sys": {"country": "TC"},
        "weather": [{"description": "cloudy"}],
        "main": {
            "temp": 20.5,
            "temp_min": 18.5,
            "temp_max": 22.5,
            "feels_like": 21.0,
            "humidity": 70,
        },
    }

    mock_get.return_value = mock_response
    weather_data = weather.get_current_weather("Test City", "TC")
    assert weather_data == mock_response.json()

@mock.patch("requests.get")
def test_weather_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response

    weather_data = weather.get_current_weather("Test City", "TC")
    assert weather_data is None