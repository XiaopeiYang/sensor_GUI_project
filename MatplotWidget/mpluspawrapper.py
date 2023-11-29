
from ast import Try
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import numpy as np
import time
from PyQt5.QtCore import QTimer
from matplotlib.lines import Line2D
from database.database import Database

Num_points_A_curve = 5


class MplUspa(FigureCanvas):
    def __init__(self, width=3.2, height=2.7):
        self.fig = Figure(figsize=(width, height), dpi=70)
        super(MplUspa, self).__init__(self.fig)
        self.ax = self.fig.add_subplot(111)  # 111表示1行1列，第一张曲线图

    def add_line(self, x_data, y_data, y2_data=None, y3_data=None, xlabel="Distance (mm)"):
        self.line = Line2D(x_data, y_data)  # 绘制2D折线图

        self.ax.grid(True)  # 添加网格
        self.ax.set_title('Sensor Data')  # 设置标题

        # 设置xy轴最大最小值,找到x_data, y_data最大最小值
        self.ax.set_xlim(np.min(x_data), np.max(x_data))
        self.ax.set_ylim(np.min(y_data), np.max(y_data) + 2)  # y轴稍微多一点，会好看一点

        self.ax.set_xlabel(xlabel)  # 设置坐标名称
        self.ax.set_ylabel('Value')


        # ------------------------------------------------------#
        self.ax.add_line(self.line)

        # second curve
        self.line2 = Line2D(x_data, y2_data)
        self.ax.add_line(self.line2)
        self.line2.set_color('red')  # 设置线条颜色

        # third curve
        self.line3 = Line2D(x_data, y3_data)
        self.ax.add_line(self.line3)
        self.line3.set_color('blue')  # 设置线条颜色

        self.ax.legend([self.line, self.line2, self.line3], [
                       'Threshold curve', 'Envelope', 'IO Line'])  # 添加图例


class MplUspaWrapper(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.pbar = QProgressBar(self)
        self.pbar.setValue(0)
        self.pbar.hide()
        self.db = Database()

        self.load_line()  # 加载动态曲线

    def load_line(self):
        self.uspa = MplUspa()
        self.vbl = QVBoxLayout()
        self.ntb = NavigationToolbar(self.uspa, None)
        self.vbl.addWidget(self.ntb)
        self.vbl.addWidget(self.uspa)
        self.setLayout(self.vbl)

        # 准备数据，绘制曲线
        
        try:
            results = self.db.read_uspadistance_db()[-Num_points_A_curve:]
            if results:
                self.uspa.add_line([i[1] for i in results], [i[3] for i in results], [
                i[4] for i in results], [i[5] for i in results], xlabel="Distance (mm)")
        except:
            print("The database not create yet, This will create the db automatically")
 
        

    def updatedata(self, x_data, y_data, y2_data, y3_data, xlabel):

        self.uspa.line.set_ydata(y_data)  # 更新数据
        self.uspa.line.set_xdata(x_data)
        self.uspa.line2.set_ydata(y2_data)
        self.uspa.line2.set_xdata(x_data)
        self.uspa.line3.set_ydata(y3_data)
        self.uspa.line3.set_xdata(x_data)
        self.uspa.ax.set_xlabel(xlabel)

        self.uspa.draw()  # 重新画图
