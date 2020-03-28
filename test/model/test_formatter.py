#-*-coding:utf-8-*
"""Formatter module test"""

import unittest
import json

from source.model.formatter import FormatterJsonWeatherClassic

class FormatterJsonWeatherClassicTest(unittest.TestCase):
    def testGiveFormatStringWeatherClassic(self):
        dataExpected = "Coord:\n\tlat:-3 lon:43\nTemp:27.12\n\tTemp min:27.12\n\tTemp max:27.12\n"
        data = '{"coord":{"lon":43,"lat":-3},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":300.269,"pressure":1024.22,"humidity":100,"temp_min":300.269,"temp_max":300.269,"sea_level":1024.19,"grnd_level":1024.22},"wind":{"speed":6.25,"deg":166.509},"clouds":{"all":92},"dt":1541328238,"sys":{"message":0.0025,"sunrise":1541299484,"sunset":1541343501},"id":0,"name":"","cod":200}'
        data = json.loads(data)

        formatter = FormatterJsonWeatherClassic(data)
        dataFormatted = formatter.formatString()

        self.assertIsNotNone(dataFormatted)
        self.assertEqual(dataExpected, dataFormatted)

    def testGiveFormatStringWeatherClassicWithoutExistingCity(self):
        dataExpected = "City not found"
        data = "{'cod': '404', 'message': 'city not found'}"

        formatter = FormatterJsonWeatherClassic(data)
        dataFormatted = formatter.formatString()

        self.assertIsNotNone(dataFormatted)
        self.assertEqual(dataExpected, dataFormatted)

