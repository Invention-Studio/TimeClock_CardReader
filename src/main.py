import SerialRead as sr
import sys
from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtGui import QHBoxLayout
from PyQt4.QtCore import Qt
 
qtCreatorFile = "mainwindow.ui"
 
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
 
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.showFullScreen()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()

    card = sr.readCard()
    print card

    sys.exit(app.exec_())
