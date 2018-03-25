import sys
from PyQt4 import QtGui, QtCore
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt4agg
from matplotlib import style

style.use('fivethirtyeight')


class Window(QtGui.QMainWindow):


    def linegraph(self, file1):
        x1,y1 = np.loadtxt(file1,delimiter=',',unpack=True)
        ax1 = plt.subplot2grid((6,6), (0,0), rowspan=2, colspan=2)
        ax1.plot(x1,y1,label='function1',color='y')
        ax1.set_title('Line Graph')
        ax1.set_xlabel('x-axis')
        ax1.set_ylabel('y-axis')
        ax1.legend()

    def bargraph(self, file2):
        x2,y2 = np.loadtxt(file2,delimiter=',',unpack=True)

        ax2 = plt.subplot2grid((6,6), (0,4), rowspan=2, colspan=2)
        ax2.bar(x2,y2,label='function2',color='b')
        ax2.set_title('Bar Graph')
        ax2.set_xlabel('x-axis')
        ax2.set_ylabel('y-axis')
        ax2.legend()

    def piechart(self, file3):

        slices = np.loadtxt(file3,delimiter=',',unpack=True)
        colors= ['c','m','r','b','y']
        products=['Product1','Product2','Product3','Product4','Product5']

        ax3 = plt.subplot2grid((6,6), (4,0), rowspan=2, colspan=2)
        ax3.pie(slices, labels=products,colors=colors,startangle=90,shadow= True,explode=(0,0.1,0,0,0),autopct='%3.2f%%')
        ax3.set_title('Pie Chart')



    def scatterplot(self, file4):
        x4,y4 = np.loadtxt(file4,delimiter=',',unpack=True)

        ax4 = plt.subplot2grid((6,6), (4,4), rowspan=2, colspan=2)
        ax4.scatter(x4,y4,label='function3',color='c')
        ax4.set_title('Scatter Plot')
        ax4.set_xlabel('x-axis')
        ax4.set_ylabel('y-axis')
        ax4.legend()


    def __init__(self):

        super(Window, self).__init__()
        self.setWindowTitle("PyQt-Graphs")
        self.setWindowIcon(QtGui.QIcon('newlogo.png'))

        self.figure  = plt.figure ()
        self.drawing = self.figure.add_subplot (111)
        self.canvas  = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg (self.figure)
        self.setCentralWidget (self.canvas)

        self.home()

        file1 = 'line.txt'
        file2 = 'bar.txt'
        file3 = 'pie.txt'
        file4 = 'scatter.txt'

        graph1 = self.linegraph(file1)
        graph2 = self.bargraph(file2)
        graph3 = self.piechart(file3)
        graph4 = self.scatterplot(file4)


    def home(self):
        self.show()

    def closeEvent(self,event):
        choice = QtGui.QMessageBox.question(self,"Exit!","Are you sure?",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.No:
            event.ignore()
        else:
            event.accept()
            sys.exit()

def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()
