#-*-coding:utf-8-*
"""Weather model"""

from source.model.formatter import FormatterJsonWeatherClassic
from source.model.readerOnline import ReaderOnlineJsonWeatherCity

class IWeatherModel:
    """Weather model interface"""
    def changeOption(self, option):
        raise NotImplementedError("Must be implemented")

    def giveJsonFormatted(self, *parameters):
        raise NotImplementedError("Must be implemented")

class WeatherModel(IWeatherModel):
    """Weather model class"""
    def __init__(self, onlineReaderJsonList):
        self._reader = onlineReaderJsonList
        self._position = 0

    def changeOption(self, option):
        if(option > -1 and option < len(self._reader)):
            self._position = option

    def giveJsonFormatted(self, *parameters):
        data = self._reader[self._position].readUrl(*parameters)
        formatterString = FormatterJsonWeatherClassic(data)

        return formatterString.formatString()
