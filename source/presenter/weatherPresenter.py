#-*-coding:utf-8-*

from source.model.readerOnline import ReaderOnlineJsonWeatherCity, ReaderOnlineJsonWeatherLatitudeLongitude
from source.model.weatherModel import WeatherModel

class IWeatherPresenter:
    """Weather presenter interface"""
    def changeOption(self, option):
        raise NotImplementedError("Must be implemented")

    def giveTemperature(self, *parameters):
        raise NotImplementedError("Must be implemented")

class WeatherPresenter(IWeatherPresenter):
    def __init__(self, model):
        self._weatherModel = model

    def changeOption(self, option):
        self._weatherModel.changeOption(option)

    def giveTemperature(self, *parameters):
        return self._weatherModel.giveJsonFormatted(*parameters)
