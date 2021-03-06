import sys
from sys import argv
from os import path
from Tkinter import *
import tkFileDialog
from PyQt4 import QtCore, QtGui, uic
from moviepy.editor import *
#import image

qtCreatorFile = 'vid2gif.ui'
(Ui_MainWindow, QtBaseClass) = uic.loadUiType(qtCreatorFile)

def main():
    global app
    app = QtGui.QApplication(sys.argv)
    window = vid2gif()
    window.show()
    app.exec_()

class vid2gif(QtGui.QMainWindow, Ui_MainWindow, QtGui.QWidget):
    global app
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        app.setStyle(QtGui.QStyleFactory.create("cleanlooks"))      

        self.btn_gen_gif.clicked.connect(self.gen_file)
        self.btn_browse_file.clicked.connect(self.browse_file)

    def gen_file(self):
        filename = self.line_filein.text()
        start = float(self.dbl_start.value()) # 1,22.65
        end = float(self.dbl_end.value())   # 1,23.2
        size = float(self.dbl_scale.value())  # 0.3
        outname = self.line_gif.text()
        clip = (VideoFileClip(str(filename))
                .subclip((start),(end))
                .resize(size))
        clip.write_gif(str(outname), fps=self.spn_fps.value(), fuzz=self.spn_fuzz.value())

    def browse_file(self):
        root = Tk()
        fileName = tkFileDialog.askopenfilename(
                filetypes=(('AVI Files', '.avi'),
                           ('MP4 Files', '.mp4'),
                           ('All Files', '.*')))
        root.destroy()
        self.line_filein.setText(path.basename(fileName))
#        root.destroy()

global app
app = QtGui.QApplication(sys.argv)
window = vid2gif()
window.show()
sys.exit(app.exec_())

#for filename in glob('*.jpg'):
#    img = Image.open(filename)
#	img.save(path.splitext(filename)[0]+'.png')




