# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'source/view/ui/weather.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 271)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.localityLabel = QtWidgets.QLabel(self.centralwidget)
        self.localityLabel.setObjectName("localityLabel")
        self.verticalLayout.addWidget(self.localityLabel)
        self.localityLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.localityLineEdit.setObjectName("localityLineEdit")
        self.verticalLayout.addWidget(self.localityLineEdit)
        self.temperatureLabel = QtWidgets.QLabel(self.centralwidget)
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.verticalLayout.addWidget(self.temperatureLabel)
        self.resultListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.resultListWidget.setObjectName("resultListWidget")
        self.verticalLayout.addWidget(self.resultListWidget)
        self.searchTemperatureButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchTemperatureButton.setObjectName("searchTemperatureButton")
        self.verticalLayout.addWidget(self.searchTemperatureButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Weather"))
        self.localityLabel.setText(_translate("MainWindow", "Insert region:"))
        self.temperatureLabel.setText(_translate("MainWindow", "Result:"))
        self.searchTemperatureButton.setText(_translate("MainWindow", "Search temperature"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

