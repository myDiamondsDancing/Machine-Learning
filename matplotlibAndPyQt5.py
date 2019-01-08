import sys
import random      # Для рандомного выбора функций

import numpy as np # Для вычислений

# Область для черчения
# Панель управления
# Фигура для черчений
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

# Импортирование необходимых виджетов
from PyQt5.Qt import *

def tg(data):
    return np.tan(data)

def ctg(data):
    return 1 / tg(data)


class PlotWidget(QWidget):

    functions = {
                1 : np.sin,
                2 : np.cos,
                3 : tg,
                4 : ctg
                }

    def __init__(self, parent=None):
        super(PlotWidget, self).__init__(parent) # Инициализируем экземпляр

        self.initUi() # Строим интерфейс

    def initUi(self):

        self.mainLayout = QVBoxLayout(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.navToolbar = NavigationToolbar(self.canvas, self)

        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def plot(self):

        function_index = random.randint(1, 4)

        function = PlotWidget.functions[function_index]

        x = np.linspace(-10, 10, 2000)

        y = function(x)

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')
        
        ax.axhline(y=0, xmin= -10.25, xmax=10.25, color='#000000')
        ax.axvline(x=0, ymin= -2, ymax=2, color='#000000')        

        ax.set_ylim([-2, 2])
        ax.set_xlim([-10.25, 10.25])
        
        if function == np.sin or function == np.cos:
            ax.axhline(y=1, xmin= -10.25, xmax=10.25, color='b', linestyle='--')
            ax.axhline(y= -1, xmin= -10.25, xmax=10.25, color='b', linestyle='--')
            
        ax.plot(x, y, linestyle='-.', color='#008000', label=function.__name__)
        ax.legend(loc='upper right')
        self.canvas.draw()    


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUi()
        self.connectUi()

    def initUi(self):
        self.centralWidget = QWidget(self)

        self.l = QVBoxLayout(self.centralWidget)
        self.bl = QHBoxLayout(self.centralWidget)

        self.plotWidget = PlotWidget()

        self.plotButton = QPushButton('Plot')
        self.clearButton = QPushButton('Clear')

        self.plotButton.setStyleSheet('font-size: 12pt; font-weight: 530;')
        self.clearButton.setStyleSheet('font-size: 12pt; font-weight: 530;')

        self.bl.addWidget(self.plotButton)
        self.bl.addWidget(self.clearButton)

        self.l.addLayout(self.bl)
        self.l.addWidget(self.plotWidget)

        self.setCentralWidget(self.centralWidget)

    def connectUi(self):
        self.plotButton.clicked.connect(self.plotWidget.plot)
        self.clearButton.clicked.connect(self.clear)

    def clear(self):
        self.plotWidget.figure.clear()
        self.plotWidget.canvas.draw()        
  
app = QApplication([])
p = MainWindow()
p.show()

sys.exit(app.exec_())
