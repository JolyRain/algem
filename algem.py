from math import sin, cos
from matplotlib import ticker
from pylab import *


# Класс, описывающий астроиду
class Astroid:
    EQUATION = r'$x^{\frac{2}{3}}+y^{\frac{2}{3}}=R^{\frac{2}{3}}$'
    ANGLE = np.linspace(0, 2 * pi, 1000)
    radius = 0
    x = 0
    y = 0

    def __init__(self, radius):
        self.radius = radius
        self.__function()

    # Параметрическое уравнение астроиды
    def __function(self):
        self.x = self.radius * pow(cos(self.ANGLE), 3)
        self.y = self.radius * pow(sin(self.ANGLE), 3)


# "Красота" для графика
def coordinate_axes():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.xaxis.set_minor_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(5))
    ax.yaxis.set_minor_locator(ticker.MultipleLocator(5))
    ax.grid(which='major',
            color='k')
    ax.minorticks_on()
    ax.grid(which='minor',
            color='gray',
            linestyle=':')
    ax.tick_params(labelsize=16)


# Класс, рисующий график астроиды
class Graphic:
    astroid = None
    BORDER = 10

    def __init__(self, astroid):
        self.astroid = astroid

    def show(self):
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot()
        ax.set_title('Астроида\n' + self.astroid.EQUATION +
                     ', при R = ' + str(self.astroid.radius), pad=15, fontsize=20)
        ax.set(xlim=[-self.BORDER, self.BORDER],
               ylim=[-self.BORDER, self.BORDER],
               )
        coordinate_axes()
        ax.plot(self.astroid.x, self.astroid.y, 'red', linewidth=3)
        plt.show()


radius_input = int(input('radius = '))
new_astroid = Astroid(radius_input)
graphic = Graphic(new_astroid)
graphic.show()
