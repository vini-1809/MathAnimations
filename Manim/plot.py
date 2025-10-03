from manim import *
from math import *

class eulernumber(Scene):
    def construct(self):
        ax = Axes(x_range=[-5,5,1],y_range=[-1,5,1])
        f1 = ax.plot(lambda x: e ** x, color= RED)
        self.add(ax,f1)
