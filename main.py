#-*-coding:utf-8-*

import sys
from PyQt5 import QtWidgets

import source.assets.util as util

from source.model.readerOnline import ReaderOnlineJsonWeatherCity, ReaderOnlineJsonWeatherLatitudeLongitude
from source.model.weatherModel import WeatherModel
from source.presenter.weatherPresenter import WeatherPresenter
from source.view.weatherView import WeatherMainView

'''
import urllib, json

url = "http://api.openweathermap.org/data/2.5/weather?q=ostende&appid=7e3a640ce07a4ed3d2752c38933c4210"
response = urllib.urlopen(url)
data = json.loads(response.read())
print(data)
'''

class Main:
    def __init__(self):
        readerOnlineCity = ReaderOnlineJsonWeatherCity(util.KEY)
        readerOnlineLatitudeLongitude = ReaderOnlineJsonWeatherLatitudeLongitude(util.KEY)
        model = WeatherModel([readerOnlineCity, readerOnlineLatitudeLongitude])

        self._weatherPresenter = WeatherPresenter(model)

        self._application = QtWidgets.QApplication(sys.argv)
        self._mainWindow = QtWidgets.QMainWindow()
        
        self._weatherView = WeatherMainView(self._mainWindow, self._weatherPresenter)

    def run(self):
        self._mainWindow.show()
        sys.exit(self._application.exec_())

if __name__ == "__main__":
    main = Main()
    main.run()
