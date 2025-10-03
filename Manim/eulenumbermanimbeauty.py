from manim import *
from math import *

class graph(Scene):
    def construct(self):
        vt= ValueTracker(-5)
        ax = Axes(x_range=[-5,5,1],y_range=[-1,5,1])
        
        f = always_redraw( lambda: ax.plot(lambda x: e ** x, color= RED, x_range=[-5,vt.get_value()]))

        f_dot= always_redraw( lambda: Dot(
            point=ax.c2p(vt.get_value(),f.underlying_function(vt.get_value())),
            color = RED
            )
        )
        self.play(Write(ax))
        self.wait()

        self.add(f,f_dot)

        self.play (vt.animate.set_value(5),run_time=6)

        self.play(FadeOut(f_dot))
        self.wait()

