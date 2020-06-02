from math import sin, cos
from pylab import *


class Cardioid:
    ANGLE = np.linspace(0, 2 * pi, 1000)
    parameter = 0
    x = 0
    y = 0

    def __init__(self, parameter):
        self.parameter = parameter
        self.__function()

    def __function(self):
        self.x = self.parameter * (2 * cos(self.ANGLE) - cos(2 * self.ANGLE))
        self.y = self.parameter * (2 * sin(self.ANGLE) - sin(2 * self.ANGLE))


def coordinate_axes():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)


class Graphic:
    cardioid = None
    BORDER = 20

    def __init__(self, cardioid):
        self.cardioid = cardioid

    def show(self):
        fig = plt.figure()
        ax = fig.add_subplot()
        ax.set(xlim=[-self.BORDER, self.BORDER],
               ylim=[-self.BORDER, self.BORDER],
               title='Кардиоида',
               )
        plt.grid()
        coordinate_axes()
        plt.plot(self.cardioid.x, self.cardioid.y, 'red', linewidth=3)
        plt.show()


param = float(input('parameter = '))
new_cardioid = Cardioid(param)
graphic = Graphic(new_cardioid)
graphic.show()
