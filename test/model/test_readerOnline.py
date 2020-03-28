#-*-coding:utf-8-*
"""Reader module online test"""

import unittest

import source.assets.util as util

from source.model.readerOnline import ReaderOnlineJsonWeatherCity, ReaderOnlineJsonWeatherLatitudeLongitude

class ReaderOnlineJsonWeatherCityTest(unittest.TestCase):
    def testGivePointPlayerA(self):
        weatherCity = ReaderOnlineJsonWeatherCity(util.KEY)
        data = weatherCity.readUrl("liege")

        self.assertIsNotNone(data)
        self.assertEqual(200, data["cod"])

class ReaderOnlineJsonWeatherLatitudeLongitudeTest(unittest.TestCase):
    def testGivePointPlayerA(self):
        weatherCity = ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)
        data = weatherCity.readUrl("50.63", "5.57")

        self.assertIsNotNone(data)
        self.assertEqual(200, data["cod"])

