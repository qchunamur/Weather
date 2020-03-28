#-*-coding:utf-8-*

import unittest

from source.model.readerOnline import ReaderOnlineJsonWeatherCity, ReaderOnlineJsonWeatherLatitudeLongitude
from source.model.weatherModel import WeatherModel
from source.presenter.weatherPresenter import WeatherPresenter

class WeatherPresneterTest(unittest.TestCase):
    def setUp(self):
        readerOnlineCity = ReaderOnlineJsonWeatherCity()
        readerOnlineLatitudeLongitude = ReaderOnlineJsonWeatherLatitudeLongitude()
        model = WeatherModel([readerOnlineCity, readerOnlineLatitudeLongitude])

        self._weatherPresenter = WeatherPresenter(model)

    def testGiveFormatStringWeatherCity(self):
        result = self._weatherPresenter.giveTemperature("spa")

        self.assertIsNotNone(result)
        self.assertNotEqual("City not found", result)

    def testGiveFormatStringWeatherLongitudeLatitude(self):
        self._weatherPresenter.changeOption(1)

        result = self._weatherPresenter.giveTemperature("150.63", "5.57")

        self.assertIsNotNone(result)
        self.assertNotEqual("City not found", result)