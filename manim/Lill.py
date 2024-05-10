from manim import *
from math import *


class MainPath(MovingCameraScene):
    def construct(self):
        
        A_coord = [0, 0, 0]
        B_coord = [1, 0, 0]
        C_coord = [1, -5, 0]
        D_coord = [-6, -5, 0]
        E_coord = [-6, -2, 0]

        hospitals_coord = [
            [1, 2, 0],
            [2, 4, 0],
            [4, 1, 0],
        ]

        self.camera.frame_center = [-2.5, -2.5, 0]

        A = Dot(point=A_coord, color="#9914ff", z_index=2)
        B = Dot(point=B_coord, color="#2881bd", z_index=2)
        C = Dot(point=C_coord, color="#2881bd", z_index=2)
        D = Dot(point=D_coord, color="#2881bd", z_index=2)
        E = Dot(point=E_coord, color="#9914ff", z_index=2)

        text = Tex("$p(x)=x^3-4x^2+5x-2$").move_to(ORIGIN).shift(0.5 * UP).shift(2.5 * LEFT)

        AB = Line(A, B, z_index=1, color=WHITE, stroke_width=5)
        BC = Line(B, C, z_index=1, color=WHITE, stroke_width=5)
        CD = Line(C, D, z_index=1, color=WHITE, stroke_width=5)
        DE = Line(D, E, z_index=1, color=WHITE, stroke_width=5)

        self.play(Create(A), Create(B), Create(C), Create(D), Create(E))
        self.play(Create(AB), Create(BC), Create(CD), Create(DE), Create(text))

        Path1 = [
            Line(Dot(point=[0, 0, 0], radius=0.001), Dot(point=[1, -1, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[1, -1, 0], radius=0.001), Dot(point=[-3, -5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[-3, -5, 0], radius=0.001), Dot(point=[-6, -2, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5)
        ]

        Path2 = [
            Line(Dot(point=[0, 0, 0], radius=0.001), Dot(point=[1, -3, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[1, -3, 0], radius=0.001), Dot(point=[-5, -5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[-5, -5, 0], radius=0.001), Dot(point=[-6, -2, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5)
        ]

        for i in range(3):
          self.play(Create(Path1[i]))

        for i in range(3):
          self.play(Create(Path2[i]))

        self.wait(3)