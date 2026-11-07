from manim import *

class animation(Scene):
    def construct(self):
        rect1 = Rectangle(height=0.5, width=0.5, fill_opacity=1).shift(LEFT * 5)
        rect2 = Rectangle(height=0.5, width=0.5, fill_opacity=1).move_to([5, 0, 0])

        # better to make an array but im lazy
        r1 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r2 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r3 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r4 = Rectangle(height=0.5, width=0.5, fill_opacity=1)
        r5 = Rectangle(height=0.5, width=0.5, fill_opacity=1)

        group = VGroup(r1, r2, r3, r4, r5)
        group.arrange() # by default, orders L->R and centers in frame
        group.set_color_by_gradient(RED, ORANGE, YELLOW_C, PURE_GREEN)

        self.play(Write(rect1))
        self.play(Write(rect2))

        group2 = VGroup(rect1, rect2)

        self.play(rect2.animate.next_to(rect1, RIGHT))
        self.play(ReplacementTransform(group2, group))

        s1 = SurroundingRectangle(group, color=WHITE)
        s2 = SurroundingRectangle(s1, color=WHITE)

        self.play(Write(s1), Write(s2, run_time=1.5))

        """my default serif font had weird mixed-height numbers. I installed a latex distribution to use
        mathtex before giving up and just changing the font. Also, better to make an array of each number here"""
        t = Text("1 2 3 4 5", font="Times New Roman").next_to(s2, UP, buff=0.3).scale(1.5)
        self.play(Write(t))

        self.play(Indicate(t[0], color=RED), Indicate(r1, color=RED, scale_factor=0.3), run_time=0.75)
        self.play(Indicate(t[1], color=RED), Indicate(r2, color=RED, scale_factor=0.3), run_time=0.75)
        self.play(Indicate(t[2], color=RED), Indicate(r3, color=RED, scale_factor=0.3), run_time=0.75)
        self.play(Indicate(t[3], color=RED), Indicate(r4, color=RED, scale_factor=0.3), run_time=0.75)
        self.play(Indicate(t[4], color=RED), Indicate(r5, color=RED, scale_factor=0.3), run_time=0.75)

        group3 = VGroup(group, t, s1, s2) # remember, group2 doesnt exist anymore. so this group has everything on screen.
        d = Dot(color=RED)

        self.play(ReplacementTransform(group3, d))
        self.play(d.animate.scale(150))
        self.play(FadeOut(d))

        self.wait(3)