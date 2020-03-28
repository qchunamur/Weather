#-*-coding:utf-8-*

from source.view.weatherUi import Ui_MainWindow

class WeatherMainView(Ui_MainWindow):
    def __init__(self, mainWindow, presenter):
        super().__init__()

        self.setupUi(mainWindow)
        self._connectEvent()

        self._weatherPresenter = presenter

    def _connectEvent(self):
        self.searchTemperatureButton.clicked.connect(self._clickSearchTemperature)

    def _clickSearchTemperature(self):
        city = self.localityLineEdit.text()
        result = self._weatherPresenter.giveTemperature(city)

        #update view
        self.resultListWidget.clear()
        self.resultListWidget.addItem(result)
