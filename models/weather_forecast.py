class WeatherForecast:
    def __init__(self, data):
        self.context = data.get('@context', [])
        self.type = data.get('type', '')
        self.geometry = data.get('geometry', {})
        self.properties = data.get('properties', {})

        # Convert periods into Period objects
        self.periods = [Period(period_data) for period_data in self.properties.get('periods', [])]

class Period:
    def __init__(self, data):
        self.number = data.get('number', 0)
        self.name = data.get('name', '')
        self.start_time = data.get('startTime', '')
        self.end_time = data.get('endTime', '')
        self.is_daytime = data.get('isDaytime', False)
        self.temperature = data.get('temperature', 0)
        self.temperature_unit = data.get('temperatureUnit', '')
        self.temperature_trend = data.get('temperatureTrend', '')
        self.probability_of_precipitation = data.get('probabilityOfPrecipitation', {}).get('value', None)
        self.dewpoint = data.get('dewpoint', {}).get('value', 0)
        self.relative_humidity = data.get('relativeHumidity', {}).get('value', 0)
        self.wind_speed = data.get('windSpeed', '')
        self.wind_direction = data.get('windDirection', '')
        self.icon = data.get('icon', '')
        self.short_forecast = data.get('shortForecast', '')
        self.detailed_forecast = data.get('detailedForecast', '')

    # def __dict__(self):
    #     return {
    #         "number": self.number,
    #         "name": self.name,
    #         "start_time": self.start_time,
    #         "end_time": self.end_time,
    #         "is_daytime": self.is_daytime,
    #         "temperature": self.temperature,
    #         "temperature_unit": self.temperature_unit,
    #         "temperature_trend": self.temperature_trend,
    #         "probability_of_precipitation": self.probability_of_precipitation,
    #         "dewpoint": self.dewpoint,
    #         "relative_humidity": self.relative_humidity,
    #         "wind_speed": self.wind_speed,
    #         "wind_direction": self.wind_direction,
    #         "icon": self.icon,
    #         "short_forecast": self.short_forecast,
    #         "detailed_forecast": self.detailed_forecast
    #     }
    