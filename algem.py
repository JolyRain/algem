from math import sin, cos
from pylab import *


class Cardioid:
    parameter = 0
    ANGLE = np.linspace(0, 2 * pi, 10000)
    x = 0
    y = 0

    def __init__(self, parameter):
        self.parameter = parameter
        self.__function()

    def __function(self):
        self.x = self.parameter * (2 * cos(self.ANGLE) - cos(2 * self.ANGLE))
        self.y = self.parameter * (2 * sin(self.ANGLE) - sin(2 * self.ANGLE))


class Graphic:
    cardioid = None
    BORDER = 50

    def __init__(self, cardioid):
        self.cardioid = cardioid

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set(xlim=[-self.BORDER, self.BORDER],
               ylim=[-self.BORDER, self.BORDER],
               title='Кардиоида',
               xlabel='ось X',
               ylabel='ось Y')
        plt.plot(self.cardioid.x, self.cardioid.y, 'red')
        plt.grid()
        plt.show()


param = float(input('parameter = '))
new_cardioid = Cardioid(param)
graphic = Graphic(new_cardioid)
graphic.show()
