from manim import *
from math import *


class MainCity(MovingCameraScene):
    def construct(self):
        
        A_coord = [0, 0, 0]
        B_coord = [5, 0, 0]
        C_coord = [5, 5, 0]
        D_coord = [0, 5, 0]

        hospitals_coord = [
            [1, 2, 0],
            [2, 4, 0],
            [4, 1, 0],
        ]

        F_coord = [3, 2.5, 0]

        self.camera.frame_center = [2.5, 2.5, 0]

        A = Dot(point=A_coord, color="#2881bd", z_index=2)
        B = Dot(point=B_coord, color="#2881bd", z_index=2)
        C = Dot(point=C_coord, color="#2881bd", z_index=2)
        D = Dot(point=D_coord, color="#2881bd", z_index=2)

        AB = Line(A, B, z_index=1, color=WHITE, stroke_width=5)
        BC = Line(B, C, z_index=1, color=WHITE, stroke_width=5)
        CD = Line(C, D, z_index=1, color=WHITE, stroke_width=5)
        DA = Line(D, A, z_index=1, color=WHITE, stroke_width=5)

        self.play(Create(A), Create(B), Create(C), Create(D))
        self.play(Create(AB), Create(BC), Create(CD), Create(DA))

        lines = []

        for i in range(4):
                
            lines.append(Line([i+1, 0, 0], [i+1, 5, 0], z_index=1, color=WHITE, stroke_width=3))
            lines.append(Line([0, i+1, 0], [5, i+1, 0], z_index=1, color=WHITE, stroke_width=3))
            self.play(Create(lines[2*i]), Create(lines[2*i+1]), run_time=0.3)

        hospitals = [
            Dot(point=hospitals_coord[0], color="#c00e4d", z_index=2),
            Dot(point=hospitals_coord[1], color="#c00e4d", z_index=2),
            Dot(point=hospitals_coord[2], color="#c00e4d", z_index=2),
        ]

        F = Dot(point=F_coord, color="#9914ff", z_index=2)

        Div1 = [
            Line(Dot(point=[0, 3.5, 0], radius=0.001), Dot(point=[1, 3.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[1, 3.5, 0], radius=0.001), Dot(point=[2, 2.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[2, 2.5, 0], radius=0.001), Dot(point=[3, 2.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5)
        ]
        Div2 = [
            Line(Dot(point=[2, 0, 0], radius=0.001), Dot(point=[2, 1, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[2, 1, 0], radius=0.001), Dot(point=[3, 2, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[3, 2, 0], radius=0.001), Dot(point=[3, 2.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5)
        ]
        Div3 = [
            Line(Dot(point=[5, 3.5, 0], radius=0.001), Dot(point=[4, 3.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5), 
            Line(Dot(point=[4, 3.5, 0], radius=0.001), Dot(point=[3, 2.5, 0], radius=0.001), z_index=1, color="#2881bd", stroke_width=5)
        ]

        self.play(Create(hospitals[0]), Create(hospitals[1]), Create(hospitals[2]))

        self.play(Create(F))

        self.play(Create(Div1[0]), Create(Div2[0]), Create(Div3[0]))
        self.play(Create(Div1[1]), Create(Div2[1]), Create(Div3[1]))
        self.play(Create(Div1[2]), Create(Div2[2]))

        self.wait(3)