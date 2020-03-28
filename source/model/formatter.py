#-*-coding:utf-8-*
"""Formatter data"""

class IFormatter:
    """Formatter data interface"""
    def formatString(self):
        raise NotImplementedError("Must be implemented")

class Formatter(IFormatter):
    """Formatter data abstract class"""
    def __init__(self, data):
        self._data = data

    def _calculateFahrenheitToCelsius(self, fahrenheit):
        return fahrenheit - 273.15

class FormatterJsonWeatherClassic(Formatter):
    """Formatter data weather classic"""
    def formatString(self):
        value = ""
        try:
            value = "Coord:\n\tlat:{} lon:{}\nTemp:{:0.2f}\n\tTemp min:{:0.2f}\n\tTemp max:{:0.2f}\n".format(self._data["coord"]["lat"],
                self._data["coord"]["lon"], self._calculateFahrenheitToCelsius(self._data["main"]["temp"]),
                self._calculateFahrenheitToCelsius(self._data["main"]["temp_min"]),
                self._calculateFahrenheitToCelsius(self._data["main"]["temp_max"]))
        except(Exception):
            value = "City not found"

        return value
