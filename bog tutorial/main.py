from manim import *

class animation(Scene):
    def construct(self):
        rect1 = Rectangle(height=0.5, width=0.5)

        self.play(Write(rect1))