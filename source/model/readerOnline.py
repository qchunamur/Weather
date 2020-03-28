#-*-coding:utf-8-*
"""Reader module online"""

import requests, json

class IReaderOnline:
    """Reader interface online"""
    def readUrl(self, *parameters):
        raise NotImplementedError("Must be implemented")

class ReaderOnline(IReaderOnline):
    """Reader abstract class online"""
    def __init__(self, key):
        self._key = key

class ReaderOnlineJsonWeatherCity(ReaderOnline):
    """Reader class json online"""
    def readUrl(self, *parameters):
        """1 parameter: city"""
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(parameters[0], self._key)
        response = requests.get(url)

        return json.loads(response.text)

class ReaderOnlineJsonWeatherLatitudeLongitude(ReaderOnline):
    def readUrl(self, *parameters):
        """2 parameters: latitude, longitude"""
        url = "http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={key}".format(latitude = parameters[0],
            longitude = parameters[1], key = self._key)
        response = requests.get(url)

        return json.loads(response.text)
