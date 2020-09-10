from manimlib.imports import *


class TitleScene(Scene):
    def construct(self):
        title = TextMobject(r"Cauchy t\'ipus\'u f\"uggv\'enyegyenletek")
        title.scale(1.8)
        title.set_color(BLUE)
        equation_1 = TexMobject(r"f\colon D\to D")
        equation_2 = TexMobject(r"f(x+y)=f(x)+f(y),\,\forall x,y \in D")
        equation_3 = TexMobject(r"D \in\{ \mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R} \}")
        equation_4 = TextMobject(r"$D = \mathbb{R}$ eset\'en $f$ folytonos.")

        group = VGroup(equation_1,equation_2,equation_3,equation_4)
        group.arrange_submobjects(DOWN)

        self.play(FadeIn(title),run_time = 2)
        self.play(title.shift , 2*UP)
        self.wait()
        for _,eq in enumerate(group):
            self.play(Write(eq),run_time = 2)
            self.wait(2)
        self.play(*[
            FadeOutAndShiftDown(eq) for eq in [title, group]
        ])


class NaturalCase(Scene):
    def construct(self):
        color_map = {"x":RED, "y":ORANGE}
        equation_1 = TexMobject(r"D = \mathbb{N}").scale(2)
        equation_2 = TexMobject(r"x = y = 0",tex_to_color_map = color_map)
        equation_3 = TexMobject("f(","x","+","y",")= f(","x",")+f(","y",")",tex_to_color_map =  color_map)
        #                         0   1   2   3   4       5    6     7   8
        equation_4 = TexMobject("f(","0","+","0",")= f(","0",")+f(","0",")",tex_to_color_map =  color_map)
        equation_2.next_to(equation_3,DOWN)

        self.play(Write(equation_1))
        equation_1.generate_target()
        equation_1.target.to_edge(UP)
        equation_1.target.scale(0.5)
        self.play(MoveToTarget(equation_1),run_time = 2)
        self.play(Write(equation_3),run_time = 2)
        self.wait()
        self.play(FadeIn(equation_2))
        
        self.play(*[Transform(equation_3[i],equation_4[i]) for i in [1,3,5,7]],FadeOut(equation_2), submobject_mode = "lagged_start")
        self.wait()
        equation_5 = TexMobject("f(","0",")=f(","0",")+f(","0",")")
        #                          0  1    2     3     4    5   6
        self.play(ReplacementTransform(VGroup(equation_3[1:4]),equation_5[1]),
                *[
                    ReplacementTransform(equation_3[i],equation_5[j]) for i,j in [(0,0),(4,2),(5,3),(6,4),(7,5),(8,6)]
                ])
        equation_6 = TexMobject("f(","0",")","=","0")
        self.play(Transform(equation_5,equation_6))
        self.wait()
        equation_7 = TexMobject(r"D = \mathbb{N},"," f(0)=0").to_edge(UP)
        self.play(ReplacementTransform(equation_1, equation_7[0]),ReplacementTransform(equation_5,equation_7[1]), submobject_mode = "lagged_start")
        self.wait()
        equation_8 = TexMobject("f(","x","+","y",")= f(","x",")+f(","y",")",tex_to_color_map =  color_map)
        equation_9 = TexMobject("f(","n","+","1",")= f(","n",")+f(","1",")")
        equation_10 = TexMobject("x = n, y = 1",tex_to_color_map =  color_map).next_to(equation_8,DOWN)

        for mob in [equation_8,equation_10]:
            self.play(Write(mob),run_time=2)
        self.play(Transform(equation_8,equation_9),FadeOut(equation_10), submobject_mode = "lagged_start")
        

        text = TextMobject(r"$ (f(n))_n$ sz\'amtani haladv\'any")
        arrow = Arrow(UP,DOWN)
        equation_11 = TexMobject(r"f(n) = nf(1),\,\forall n\in\mathbb{N}")

        group = VGroup(text,arrow,equation_11).arrange_submobjects(DOWN)

        self.play(equation_8.next_to, group, UP)
        self.play(FadeInFromDown(text),run_time = 2)
        self.wait()
        self.play(FadeIn(arrow))
        self.play(Write(equation_11),run_time = 4)

        self.play(*[FadeOut(mob) for mob in self.mobjects])


class IntegerCase(Scene):
    def construct(self):
        color_map = {"x":RED, "y":ORANGE}
        title = TexMobject(r"D = \mathbb{Z}").scale(2)
        
        equation_1 = TexMobject(r"f\colon\mathbb{N}\to\mathbb{N},")
        equation_2 = TexMobject(r"f(x+y)=f(x)+f(y),\,\forall x,y\in\mathbb{N}")
        equation_3 = TexMobject(r"\Downarrow").scale(1.5)
        equation_4 = TexMobject(r"f(n) = nf(1),\,\forall n\in\mathbb{N}")
        equation_5 = TexMobject(r"\mathbb{N}\subset\mathbb{Z}")
        equation_6 = equation_4.deepcopy()
        equation_7 = TexMobject("f(","x ","+","y",")=f(","x",")+","f(","y",")",tex_to_color_map = color_map)
        equation_8 = TexMobject("x = n, y = -n",tex_to_color_map = color_map).next_to(equation_7,DOWN)
        equation_9 = TexMobject("f(","n ","-","n",")=f(","n",")+","f(","-n",")")
        equation_10= TexMobject("f(","0",")=f(","n",")+","f(","-n",")")
        equation_11= TexMobject("0","=f(","n",")+","f(","-n",")")
        equation_12= TexMobject("f(-n) = -f(n)")
        equation_13= TexMobject(r"f(z) = zf(1),\,\forall z\in\mathbb{Z}")

        group_1 = VGroup(equation_1,equation_2,equation_3,equation_4).arrange_submobjects(DOWN)
        surrounding_rectangle_1 = SurroundingRectangle(group_1)
    
        self.play(Write(title))
        self.wait()
        title.generate_target()
        title.target.to_edge(UP).scale(0.5)
        self.play(MoveToTarget(title))

        self.play(ShowCreation(surrounding_rectangle_1))
        self.play(FadeIn(group_1),run_time = 1)
        self.wait()

        natural_case = VGroup(surrounding_rectangle_1,group_1)
        
        natural_case.generate_target()
        natural_case.target.shift(3*LEFT).scale(0.6)
        self.play(MoveToTarget(natural_case))

        implication = VGroup(equation_5,Arrow(LEFT,RIGHT)).arrange(DOWN).next_to(natural_case,RIGHT).shift(0.25*UP)
        self.play(Write(implication))
        self.wait()
        equation_6.next_to(implication,RIGHT).shift(0.25*DOWN)
        self.play(ReplacementTransform(equation_4.deepcopy(),equation_6),run_time = 1.5)
        self.wait()
        title_bar = VGroup(title,equation_6)
        title_bar.generate_target()
        title_bar.target.arrange_submobjects(RIGHT,buff = 0.5)
        title_bar.target.to_edge(UP)

        self.play(MoveToTarget(title_bar), *[FadeOut(mobj) for mobj in [natural_case, implication]],run_time = 1.5)

        for mobj in [equation_7,equation_8]:
            self.play(Write(mobj))
        self.wait()
        self.play(ReplacementTransform(equation_7,equation_9),FadeOut(equation_8),submobject_mode = "lagged_start")
        self.play(ReplacementTransform(VGroup(equation_9[1:4]),equation_10[1]),
            *[
                ReplacementTransform(equation_9[i],equation_10[j]) for i,j in [(0,0),(4,2),(5,3),(6,4),(7,5),(8,6),(9,7)]
            ])
        self.play(ReplacementTransform(VGroup(equation_10[:2]),equation_11[0]),
        *[
            ReplacementTransform(equation_10[i],equation_11[i-1]) for i in [2,3,4,5,6,7]
        ])
        arrow = Arrow(UP,DOWN)
        equation_11.generate_target()
        VGroup(equation_11.target,arrow,equation_12).arrange_submobjects(DOWN)
        self.play(MoveToTarget(equation_11))
        self.play(FadeIn(arrow))
        self.play(Write(equation_12))
        self.wait(1)
        group_3 = VGroup(equation_6,equation_12)
        group_3.generate_target()
        group_3.target.arrange_submobjects(DOWN)
        group_3.target.shift(3*LEFT)
        arrow.generate_target()
        arrow.target.rotate(PI/2)
        arrow.target.next_to(group_3.target,RIGHT)
        title.generate_target()
        position =title.get_center()
        title.target.move_to(np.array([0,position[1],0]))
        title.target.to_edge(UP)
        self.play(*[MoveToTarget(mobj) for mobj in [group_3,arrow,title]], FadeOut(equation_11),run_time = 1.5)
        equation_13.next_to(arrow)
        self.wait()
        self.play(Write(equation_13),run_time = 1.5)
        self.wait()


class RationalCase(Scene):
    def construct(self):
        color_map = {"x":RED, "y":ORANGE}
        title = TexMobject(r"D = \mathbb{Q}").scale(2)
        
        self.play(Write(title))
        self.wait()
        title.generate_target()
        title.target.to_edge(UP).scale(0.5)
        self.play(MoveToTarget(title))

        equation_1 = TexMobject(r"n\in\mathbb{N} \mbox{ \'es } x_1,\ldots,x_n\in\mathbb{Q}")
        equation_2 = TexMobject(r"\Downarrow").scale(1.5)
        equation_3 = TexMobject(r"f\left(\sum^n_{k=1}","x_k",r"\right) = \sum^n_{k=1}f(","x_k",")")
        equation_4 = TexMobject(r"f\big(\sum^n_{k=1}",r"\frac{m}{n}",r"\big) = \sum^n_{k=1}f\big(",r"\frac{m}{n}",r"\big)")
        equation_5 = TexMobject(r"f\big(",r"n\cdot\frac{m}{n}",r"\big) = nf\big(",r"\frac{m}{n}",r"\big)")
        equation_6 = TexMobject(r"f\big(",r"m",r"\big) = nf\big(",r"\frac{m}{n}",r"\big)")
        equation_7 = TexMobject(r"mf\big(",r"1",r"\big) = nf\big(",r"\frac{m}{n}",r"\big)")
        equation_8 = TexMobject(r"\frac{m}{n}f(","1",r"\big) = f\big(",r"\frac{m}{n}",r"\big)")
        equation_9 = TexMobject(r"f(q) = qf(1),\,\forall q\in\mathbb{Q}")

        group_1 = VGroup(equation_1,equation_2,equation_3).arrange_submobjects(DOWN)
        times = [1.5,0.5,2]
        for i,mobj in enumerate(group_1):
            self.play(Write(mobj),run_time = times[i])
            if (i!=1) :
                self.wait()
        
        self.play(*[FadeOut(mob) for mob in [equation_1,equation_2]])

        substitution = VGroup(Arrow(UP,DOWN).scale(0.75),TexMobject(r"x_k =",r" \frac{m}{n}").scale(0.75)).arrange_submobjects(RIGHT)
        equation_3.generate_target()
        VGroup(equation_3.target,substitution, equation_4).arrange_submobjects(DOWN)
        self.play(MoveToTarget(equation_3))
        self.play(Write(substitution))
        self.wait()
        self.play(*[ReplacementTransform(equation_3[i].deepcopy(),equation_4[j]) for i,j in [(0,0),(2,2),(4,4)]])
        self.play(*[ReplacementTransform(substitution[1][1].deepcopy(),equation_4[i]) for i in [1,3]])
        self.wait()
        self.play(*[FadeOut(mob) for mob in [substitution, equation_3]], equation_4.move_to, ORIGIN)
        self.wait()
        self.play(*[ReplacementTransform(equation_4[i],equation_5[i]) for i in [0,1,2,3,4]])
        self.play(ReplacementTransform(equation_5,equation_6))
        self.play(ReplacementTransform(equation_6,equation_7))
        self.play(ReplacementTransform(equation_7,equation_8))
        self.wait(2)
        self.play(ReplacementTransform(equation_8,equation_9))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        

class RealCase(Scene):
    def construct(self):
        title = TextMobject(r"$D = \mathbb{R}$ \'es $f$ folytonos").scale(2)
        
        self.play(Write(title))
        self.wait()
        title.generate_target()
        title.target.to_edge(UP).scale(0.5)
        self.play(MoveToTarget(title))

        equation_1 = TexMobject(r"f\colon\mathbb{Q}\to\mathbb{Q},")
        equation_2 = TexMobject(r"f(x+y) = f(x)+f(y),\,\forall x,y\in\mathbb{Q}")
        equation_3 = TexMobject(r"\Downarrow").scale(1.5)
        equation_4 = TexMobject(r"f(q) = qf(1),\,\forall q\in\mathbb{Q}")
        equation_5 = equation_4.deepcopy()
        equation_6 = TextMobject(r"$\mathbb{Q}$ s\H ur\H u $\mathbb{R}-ben$")
        equation_7 = TexMobject(r"\forall x\in\mathbb{R}, \exists (q_n)_n\subset\mathbb{Q}: q_n\to x")
        equation_8 = TexMobject(r"\Updownarrow")
        equation_9 = TextMobject(r"$f$ folytonos $x$-ben")
        equation_10 = TexMobject(r"\forall (x_n)_n\subset\mathbb{R}: x_n\to x \Rightarrow f(x_n)\to f(x)")
        equation_11 = TexMobject(r"f(q_n)",r"\to f(x)")
        equation_12 = TexMobject(r"q_nf(1)",r"\to f(x)")
        equation_13 = TexMobject(r"xf(1)=f(x)")
        equation_14 = TexMobject(r"f(x) = xf(1),\,\forall x\in\mathbb{R}")
        dense_set = VGroup(equation_6,equation_8,equation_7)
        rational_group = VGroup(equation_1,equation_2,equation_3,equation_4).arrange_submobjects(DOWN) 
        surround = SurroundingRectangle(rational_group)
        self.play(ShowCreation(surround))
        self.play(FadeIn(rational_group),run_time = 1.5)
        rational_case = VGroup(surround,rational_group)
        self.wait()
        rational_case.generate_target()
        rational_case.target.scale(0.7).shift(3*LEFT)
        self.play(MoveToTarget(rational_case))
        implication = VGroup(Arrow(LEFT,RIGHT),TexMobject(r"\mathbb{Q}\subset\mathbb{R}")).arrange_submobjects(UP).next_to(rational_case,RIGHT).shift(0.25*UP)
        self.play(FadeIn(implication))
        self.wait()
        equation_5.next_to(implication).shift(0.25*DOWN)
        self.play(ReplacementTransform(equation_4.deepcopy(),equation_5),run_time = 1.5)
        self.wait()
        title_bar = VGroup(title,equation_5)
        title_bar.generate_target()
        title_bar.target.arrange_submobjects(RIGHT, buff = 0.5)
        title_bar.target.to_edge(UP)
        self.play(MoveToTarget(title_bar),*[FadeOut(mob) for mob in [rational_case, implication]])
        self.wait()
        dense_set.arrange(DOWN)
        self.play(Write(equation_6),run_time = 1.5)
        self.play(FadeInFromPoint(equation_8, equation_8.get_center()))
        self.play(Write(equation_7),run_time = 2)
        self.wait(3)
        surround_2 = SurroundingRectangle(dense_set)
        self.play(ShowCreation(surround_2))
        dense_case = VGroup(surround_2, dense_set)
        dense_case.generate_target()
        dense_case.target.shift(1.5*UP)
        self.play(MoveToTarget(dense_case))
        continuous_set = VGroup(equation_9, equation_8.deepcopy(), equation_10).arrange_submobjects(DOWN).shift(DOWN)
        surround_3 = SurroundingRectangle(continuous_set)
        continuous_case = VGroup(surround_3,continuous_set)
        self.play(Write(equation_9),run_time = 1.5)
        self.play(FadeIn(continuous_set[1]))
        self.play(Write(equation_10),run_time = 2)
        self.play(ShowCreation(surround_3))
        self.wait(2)
        for mob in [dense_case, continuous_case]:
            mob.generate_target()
            mob.target.shift(3*LEFT)
            mob.target.scale(0.75)
        self.play(*[
            MoveToTarget(mob) for mob in [dense_case, continuous_case]
        ])
        dot = Dot().next_to(dense_case,RIGHT)
        arrow_1 = Arrow(dot.get_center(), np.array([2,0.1,0]))
        dot.next_to(continuous_case,RIGHT)
        arrow_2 = Arrow(dot.get_center(),np.array([2,-0.1,0]))
        arrows = VGroup(arrow_1,arrow_2)
        self.play(FadeIn(arrows))
        equation_11.next_to(arrows,RIGHT).shift(0.25*DOWN)
        self.play(Write(equation_11))
        self.wait()

        equation_12.next_to(arrows,RIGHT).shift(0.25*DOWN)
        arrow_3 = Arrow(equation_5.get_center()+0.25*DOWN, equation_11[0].get_center()+0.25*UP)
        self.play(FadeIn(arrow_3))
        self.play(ReplacementTransform(equation_11,equation_12))
        self.wait(1)

        alternate_limit = VGroup(TexMobject(r"\downarrow"),TexMobject(r"xf(1)")).arrange_submobjects(DOWN).next_to(equation_12[0],DOWN, buff = 0.05)
        self.play(Write(alternate_limit))

        surround_4 = SurroundingRectangle(VGroup(equation_12,alternate_limit)).set_color(BLUE)
        self.play(ShowCreation(surround_4))
        arrow_4 = Arrow(UP,DOWN).scale(0.5).next_to(surround_4,DOWN)
        self.play(FadeIn(arrow_4))
        equation_13.next_to(arrow_4,DOWN)
        self.play(Write(equation_13))
        self.wait(2)

        pos = title.get_center()
        title.generate_target()
        title.target.move_to(np.array([0,pos[1],0]))
        self.play(Transform(VGroup(dense_case,continuous_case,arrows,arrow_3,alternate_limit,surround_4,arrow_4,equation_13,equation_12,equation_5),equation_14),
                MoveToTarget(title))
        self.wait()


class FinalScene(Scene):
    def construct(self):
        title = TextMobject(r"Cauchy t\'ipus\'u f\"uggv\'enyegyenletek")
        title.scale(1.8)
        title.set_color(BLUE)
        equation_1 = TexMobject(r"f\colon D\to D")
        equation_2 = TexMobject(r"f(x+y)=f(x)+f(y),\,\forall x,y \in D")
        equation_3 = TexMobject(r"D \in\{ \mathbb{N},\mathbb{Z},\mathbb{Q},\mathbb{R} \}")
        equation_4 = TextMobject(r"$D = \mathbb{R}$ eset\'en $f$ folytonos.")
        equation_5 = TexMobject(r"f(x) = xf(1),\,\forall x\in D")

        group = VGroup(equation_1,equation_2,equation_3,equation_4)
        group.arrange_submobjects(DOWN)

        self.play(FadeIn(title),run_time = 2)
        self.play(title.shift , 2*UP)
        self.wait()
        for _,eq in enumerate(group):
            self.play(Write(eq),run_time =1.5)
            self.wait(2)
        equation_5.next_to(group,DOWN)
        group_1 = VGroup(equation_5,SurroundingRectangle(equation_5).set_color(RED))
        self.play(Write(group_1))
        self.wait(3)
        self.play(*[
            FadeOutAndShiftDown(eq) for eq in [title, group,group_1]
        ])





        








        





        
        
        