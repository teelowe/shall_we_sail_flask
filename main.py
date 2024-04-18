from flask import Flask, render_template
from controllers import controller

app = Flask(__name__)

@app.route('/')
def index():
  forecast = controller.Controller.get_weather_forecast()
  tides = controller.Controller.get_tides()
  return render_template("index.html", periods=forecast.periods, tides=tides.predictions)
  
if __name__ == "__main__":
  app.run(debug=True)



