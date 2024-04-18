import requests
from models import weather_forecast, tide_prediction
from datetime import datetime, timedelta

class Controller:    
    
  def get_weather_forecast():
    weather_response = requests.get("https://api.weather.gov/gridpoints/MTR/72,126/forecast")
    weather_data_json = weather_response.json()
    return weather_forecast.WeatherForecast(weather_data_json)
  
  def get_tides():
    today = datetime.today()
    one_week_from_today = today + timedelta(days=7)
    tides_response = requests.get("https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?begin_date={}&end_date={}&station=9415339&product=predictions&datum=MLLW&time_zone=lst_ldt&interval=hilo&units=english&application=DataAPI_Sample&format=json".format(today.strftime("%Y%m%d"), one_week_from_today.strftime("%Y%m%d")))
    tides_data_json = tides_response.json()
    return tide_prediction.TidePredictions(tides_data_json)
