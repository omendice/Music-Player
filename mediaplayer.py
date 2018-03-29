import sys
from PyQt4 import QtCore, QtGui, uic
import pygame

form_class = uic.loadUiType("mediaplayer.ui")[0]

class MainWindow(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.PlayButton.clicked.connect(self.PlayButtons)
        
    def PlayButtons(self):
        if (self.PlayButton.text() == "Play"):
            self.PlayButton.setText("Play")
            pygame.mixer.init()
            pygame.mixer.music.load("02 Strawberry Swing.mp3")
            pygame.mixer.music.play()
        else:
            pygame.mixer.music.pause()
            self.PlayButton.setText("Play")

app = QtGui.QApplication(sys.argv)
myWindow = MainWindow()
myWindow.show()
app.exec_()
