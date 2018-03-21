import sys
from PyQt4 import QtCore, QtGui, uic
#import eyed3

form_class = uic.loadUiType("mediaplayer.ui")[0]
#curr=eyed3.load("")

class MainWindow(QtGui.QMainWindow, form_class):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushbutton.clicked.connect(self.PlayButton)
    def PlayButton(self):
        if (self.Play.text() == "Play"):
            self.Play.setText("Pause")
            mixer.init()
            mixer.music.load('Music.mp3')
            mixer.music.play()
            #self.articstcell.setText(curr.tag.artist)
            #self.Play.clicked.connect(self.Play_clicked)
        else:
            mixer.music.pause()
            self.Play.setText("Play")
        
app = QtGui.QApplication(sys.argv)
myWindow = MainWindow()
myWindow.show()
app.exec_()
