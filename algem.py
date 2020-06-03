from math import sin, cos
from matplotlib import ticker
from pylab import *


# Класс, описывающий астроиду
class Astroid:
    EQUATION = None
    ANGLE = np.linspace(0, 2 * pi, 1000)
    is_evolute = False
    parameter_a = 0
    parameter_b = 0
    x = 0
    y = 0

    def __init__(self, parameter_a, parameter_b=None):
        self.parameter_a = parameter_a
        if parameter_b is None:
            self.parameter_b = parameter_a
        else:
            self.parameter_b = parameter_b
            self.is_evolute = True
        self.__set_equation()
        self.__function()

    # Параметрическое уравнение астроиды
    def __function(self):
        self.x = self.parameter_a * pow(cos(self.ANGLE), 3)
        self.y = self.parameter_b * pow(sin(self.ANGLE), 3)

    def __set_equation(self):
        self.EQUATION = r'$x=a\cos^{3}\left(t\right)$, ' + r'$y=b\sin^{3}\left(t\right)$' \
            if self.is_evolute else \
            r'$x=R\cos^{3}\left(t\right)$, ' + r'$y=R\sin^{3}\left(t\right)$'


# "Красивое" поле для графика
def coordinate_axes():
    ax = plt.gca()
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
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
    ax.tick_params(labelsize=20)


# Класс, рисующий график астроиды
class Graphic:
    title = None
    astroid = None
    BORDER = 10

    def __init__(self, astroid):
        self.astroid = astroid
        self.title = 'Астроида\n' + self.astroid.EQUATION + ('\nпри a = ' + str(
            self.astroid.parameter_a) + ' и b = ' + str(
            self.astroid.parameter_b) if self.astroid.is_evolute else '\nпри R = ' + str(self.astroid.parameter_a))

    def show(self):
        fig = plt.figure(figsize=(self.BORDER, self.BORDER))
        ax = fig.add_subplot()
        ax.set_title(self.title, pad=20, fontsize=30)
        ax.set(xlim=[-self.BORDER, self.BORDER],
               ylim=[-self.BORDER, self.BORDER])
        coordinate_axes()
        ax.plot(self.astroid.x, self.astroid.y, 'red', linewidth=3)
        plt.show()


new_astroid = Astroid(2, 10)
graphic = Graphic(new_astroid)
graphic.show()
