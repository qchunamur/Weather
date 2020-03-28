#-*-coding:utf-8-*
"""
Weather module test
"""

import unittest
import json

import source.assets.util as util

from source.model.readerOnline import ReaderOnlineJsonWeatherCity, ReaderOnlineJsonWeatherLatitudeLongitude
from source.model.weatherModel import WeatherModel

class FormatterJsonWeatherModelTest(unittest.TestCase):
    def testGiveFormatStringWeatherCity(self):
        weather = WeatherModel([ReaderOnlineJsonWeatherCity(util.KEY), ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)])
        dataFormatted = weather.giveJsonFormatted("liege")

        self.assertIsNotNone(dataFormatted)
        self.assertNotEqual("City not found", dataFormatted)

    def testGiveFormatStringWeatherLongitudeLatitude(self):
        weather = WeatherModel([ReaderOnlineJsonWeatherCity(util.KEY), ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)])

        weather.changeOption(1)

        dataFormatted = weather.giveJsonFormatted("50.63", "5.57")

        self.assertIsNotNone(dataFormatted)
        self.assertNotEqual("City not found", dataFormatted)

    def testGiveFormatStringWeatherCityNoChangeOptionLess(self):
        weather = WeatherModel([ReaderOnlineJsonWeatherCity(util.KEY), ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)])

        weather.changeOption(-1)

        dataFormatted = weather.giveJsonFormatted("liege")

        self.assertIsNotNone(dataFormatted)
        self.assertNotEqual("City not found", dataFormatted)

    def testGiveFormatStringWeatherCityNoChangeOptionMore(self):
        weather = WeatherModel([ReaderOnlineJsonWeatherCity(util.KEY), ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)])

        weather.changeOption(10000)

        dataFormatted = weather.giveJsonFormatted("liege")

        self.assertIsNotNone(dataFormatted)
        self.assertNotEqual("City not found", dataFormatted)
