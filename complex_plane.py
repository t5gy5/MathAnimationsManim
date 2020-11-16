from manimlib.imports import *

import cmath

def ArcAngleBetweenThreePoints(start,middle,end):
    def norm_squared(A,B):
        return sum([x*x for x in (B-A)])
    AC2 = norm_squared(start,end)
    AB2 = norm_squared(start,middle)
    BC2 = norm_squared(middle,end)
    cosine_angle = (AC2-AB2-BC2)/(2*math.sqrt(AB2*BC2))
    sign = -1
    if cross(end-start,middle-start)[2] < 0: #is middle to the right of the vector (start, end)
        sign = 1
    #floating point numbers are the worst
    if cosine_angle<-1 :
        return  sign*TAU
    elif cosine_angle>1:
        return 0
    else:
        return sign*2*math.acos(cosine_angle)

def ArcBetweenThreePoints(start,middle,end):
    Angle = ArcAngleBetweenThreePoints(start,middle,end)
    return ArcBetweenPoints(start, end, angle = Angle)
    
def ApplyMoebius(mobius_parameters, arc):
    start,end = arc.get_start_and_end()
    middle = arc.point_from_proportion(0.5)
    def mobius_function(z):
        a,b,c,d = mobius_parameters
        return (a*z+b)/(c*z+d)
    points = [np.array([image.real,image.imag,0]) for image in map(lambda p: mobius_function(p[0]+1j*p[1]), [start, middle, end])]
    return ArcBetweenThreePoints(*points).match_style(arc)

class ComplexScene(Scene):
    def construct(self):
        axes = [Line(10*direction,0.01*direction) for direction in [LEFT,RIGHT,UP,DOWN]]
        grid_UR = self.get_grid(RIGHT,UP,[RED_E,YELLOW_E, RED_A,YELLOW_A])
        grid_UL = self.get_grid(UP,LEFT, [BLUE_E,TEAL_E,BLUE_A,TEAL_A])
        grid_DR = self.get_grid(DOWN,RIGHT,[GREEN_E,MAROON_E,GREEN_A,MAROON_A])
        grid_DL = self.get_grid(DOWN,LEFT,[PURPLE_E,GOLD_E,PURPLE_A,GOLD_A])
        grid = [*grid_UR,*grid_UL,*grid_DR,*grid_DL,*axes]
        circle = Circle().set_color(DARK_BLUE)
        question = TextMobject(r"M$i$lyen matemat$i$ka$i$ fogalom van a h\'att\'erben?",tex_to_color_map = {"$i$":YELLOW})
        grid_with_circle = [circle,*grid]

        self.wait()
        self.play(*[ShowCreation(mobj) for mobj in grid_with_circle],run_time = 2, rate_func = double_smooth)
        self.wait(2)

        self.play(Rotate(VGroup(*grid_with_circle), angle =2*PI/3, about_point = ORIGIN), run_time =6, rate_func = there_and_back_with_pause)
        self.wait(2)
        self.play(VGroup(*grid_with_circle).shift, np.array([1,2,0]), run_time =6, rate_func = there_and_back_with_pause)
        self.wait(2)
        self.play(ApplyComplexFunction((lambda z: z*(2+3*1j)),VGroup(*grid_with_circle)),run_time =6, rate_func = there_and_back_with_pause)
        self.wait(2)
        self.play(ApplyComplexFunction((lambda z: z*z), VGroup(*grid_with_circle)),run_time =6, rate_func = there_and_back_with_pause)
        self.wait(2)
        
        self.play(*[ApplyFunction((lambda arc: ApplyMoebius([0,1,1,0],arc)),mob) for mob in grid], run_time = 6, rate_func = there_and_back_with_pause)
        
        self.play(*[FadeOut(mob) for mob in [axes[0],*grid_UL,*grid_DL, circle]], VGroup(*axes[2:]).set_color,BLUE_E,run_time =2)
        for moebius_parameters in [[1,1,0,1],[0,1,1,0],[1,-0.5,0,1],[2,0,0,1], [-1,1,1,1]]:
            self.play(*[ApplyFunction((lambda arc: ApplyMoebius(moebius_parameters,arc)),mob) for mob in [*grid_UR,*grid_DR,*axes[1:] ] ], run_time = 3)
            self.wait()

        self.play(FadeIn(VGroup(axes[0],*grid_UL,*grid_DL, circle)), VGroup(*axes[2:]).set_color,WHITE,run_time =2)
        self.play(*[ApplyFunction((lambda arc: ApplyMoebius([-5,5*1j,1j+2,1],arc)),mob) for mob in grid_with_circle], run_time = 8, rate_func = there_and_back_with_pause)
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

        self.play(Write(question))
        self.wait(2)
        self.play(FadeOutAndShiftDown(question))
        
    def get_grid(self, horizontal_dir, vertical_dir, colors):
        return [*[Line(0.01*horizontal_dir+i*vertical_dir, 20*horizontal_dir + i*vertical_dir).set_color(colors[0]) for i in range(1,10)],
                               *[Line(0.01*horizontal_dir+0.5*i*vertical_dir,20*horizontal_dir + 0.5*i*vertical_dir, stroke_width = 1).set_color(colors[1]) for i in range(1,19,2)],
                               *[Line(0.01*vertical_dir + i*horizontal_dir, 20*vertical_dir + i*horizontal_dir).set_color(colors[2]) for i in range(1,10)],
                               *[Line(0.01*vertical_dir+ 0.5*i*horizontal_dir, 20*vertical_dir + 0.5*i*horizontal_dir,stroke_width = 1).set_color(colors[3]) for i in range(1,19,2)]]


class TestArc0(Scene):
    def construct(self):
        Angle = Dot()
        arc = ArcBetweenPoints(2*RIGHT,UP,angle = 0)
        decimal = DecimalNumber(0,num_decimal_phases = 3, include_sign = True, unit = None)

        arc.add_updater(lambda mob: mob.become(ArcBetweenPoints(2*RIGHT,UP,angle = Angle.get_center()[0])))
        decimal.add_updater(lambda d: d.set_value(Angle.get_center()[0]).next_to(Angle))

        self.add(arc,decimal,Angle)
        self.wait()
        self.play(Angle.shift, (TAU*RIGHT), run_time = 6)
        self.wait()

class TestArc1(Scene):
    def construct(self):
        points = [DOWN,-2*UP,2*RIGHT]
        arc = ArcBetweenThreePoints(*points)

        self.add(arc,*[Dot(p) for p in points])

class TestArc2(Scene):
    def construct(self):
        line = Line(np.array([-1,3,0]), np.array([1,-2,0]))
        circle = Circle(radius = 2).set_color(BLUE_E)
        self.add(line,circle)
        self.wait()
        self.play(*[ApplyFunction((lambda arc: ApplyMoebius([0,1,1,0],arc)),mob) for mob in [line, circle]], run_time = 4, rate_func = there_and_back_with_pause)
        self.wait()
        self.play(*[FadeOut(m) for m in self.mobjects])

