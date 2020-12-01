from manimlib.imports import *


class ShowTrick(Scene):
    def setup(self):
        self.cards = [ImageMobject("D:\\AnimatedMath\\manim\\media\\assets\\raster_images\\"+ str(digit) + letter +".png") for  digit in range(2,9) for letter in ["C","D","H","S"]]
        self.cards.pop(len(self.cards)-1)
        perm = [18, 5, 9, 1, 25, 20, 21, 10, 19, 22, 15, 8, 12, 13, 16, 3, 0, 2, 7, 17, 23, 6, 26, 11, 24, 4, 14]
        self.cards = [self.cards[perm[i]].to_corner(UL) for i in range(27)]
        self.cover = ImageMobject("D:\\AnimatedMath\\manim\\media\\assets\\raster_images\\cover.png").to_corner(UL)

    def construct(self):
        current_position = 18
        target_position = 20
        covers = [self.cover.deepcopy().move_to(ORIGIN) for _ in range(27)]
        group = Group(*covers)
        text = TextMobject(r"V\'alassz egy k\'arty\'at!").to_edge(UP,buff = 1.5)
        answer = TexMobject(str(target_position)).scale(2).shift(DOWN)
        title = TextMobject(r"A $27$-es k\'artya tr\"ukk").scale(2)
        choosen_card = self.cards[current_position].deepcopy().move_to(ORIGIN).to_edge(DOWN,buff = -1)
        self.play(Write(title))
        self.wait()
        self.play(AnimationGroup(FadeOut(title),FadeIn(group),lag_ratio = 0.9))
        self.play(ApplyMethod(group.arrange_submobjects, RIGHT, {"buff":-1}), run_time = 2)
        self.play(Write(text))
        self.wait()
        #pull out random card
        self.play(covers[current_position].shift, 5*DOWN, run_time = 2)
        self.play(FadeInFromDown(choosen_card), run_time = 2)
        #place choosen card in the corner as memory
        memory = choosen_card.deepcopy().scale(0.5).to_corner(DR)
        surround_memory = SurroundingRectangle(memory)
        self.play(ReplacementTransform(choosen_card.deepcopy(),memory), ShowCreation(surround_memory))
        #replace card
        self.play(FadeOutAndShiftDown(choosen_card),run_time = 2)
        self.play(covers[current_position].shift,5*UP,run_time = 2)
       
        #shuffle deck
        self.play(Transform(text, TextMobject("Most megkeverem a paklit...").to_edge(UP,buff = 1.5)))

        pull_outs = [
            [1, 3, 4, 5, 13, 14, 16, 19, 20, 22, 23, 24, 25, 26], 
            [1, 3, 5, 6, 7, 8, 11, 14, 15, 17, 19, 20, 24, 26], 
            [2, 3, 4, 9, 10, 11, 12, 13, 14, 15, 16, 18, 21, 26], 
            [3, 5, 8, 9, 12, 13, 14, 15, 16, 17, 18, 20, 21, 23], 
            [0, 2, 4, 5, 8, 9, 12, 14, 15, 17, 18, 21, 24, 25], 
            [0, 3, 4, 7, 8, 9, 11, 12, 13, 14, 18, 19, 21, 25], 
            [0, 1, 3, 4, 6, 10, 11, 13, 14, 17, 22, 24, 25, 26]]
        
        for pulls in pull_outs:
            group_1 = Group(*[covers[i] for i in pulls])
            self.play(group_1.shift,3.5*DOWN,run_time = 0.25)
            self.play(*[ApplyMethod(mob.shift, mob.get_center()[0]*LEFT) for mob in covers], run_time = 0.25)
            self.play(group_1.shift,3.5*UP,run_time = 0.25)
            self.play(ApplyMethod(group.arrange_submobjects,RIGHT,{"buff" :-1}), run_time = 0.25)
        #move deck to the Upper Left Corner
        self.play(*[ApplyMethod(mob.to_corner, UL) for mob in covers])
        self.add(*self.cards,self.cover)
        self.remove(*covers)
        #ask for number
        self.play(Transform(text, TextMobject(r"V\'alassz egy eg\'esz sz\'amot $1$ \'es $27$ k\"oz\"ott!").to_edge(UP,buff = 1.5)))
        self.wait()
        self.play(Write(answer))
        self.wait()
        answer.generate_target()
        answer.target.scale(0.5).next_to(memory,UP,buff = 0.5)
        answer_surround = SurroundingRectangle(answer.target).set_color(ORANGE)
        self.play(MoveToTarget(answer),ShowCreation(answer_surround),run_time = 1.5)
        self.play(Uncreate(text))
        #deal cards in packs
        x = current_position
        y = target_position-1
        for _ in range(3):
            for j in range(9):
                for i in range(3):
                    if j==8 and i==2:
                        self.remove(self.cover)
                    self.play(self.cards[3*j+i].move_to,3*RIGHT*(i-1)+DOWN*0.5*(j-3))
            text = TextMobject(r"Melyik csom\'oban van a k\'arty\'ad?").to_edge(UP,buff = 0.75)
            self.play(Write(text))
            self.wait()
            choosen_pack = x % 3
            pack_position = y % 3
            x = 9*pack_position + (x//3)
            y = y//3
            self.play(ShowCreationThenDestructionAround(Group(*[self.cards[3 * n + choosen_pack] for n in range(9)])), run_time = 2)
            self.play(FadeOut(text), *[ApplyMethod(card.shift, card.get_center()[1]*DOWN) for card in self.cards])
            self.wait()
            packs = [[self.cards[3*i+j] for i in range(9)] for j in range(3)]
            self.play(*[ApplyMethod(Group(*packs[(choosen_pack+i)%3]).move_to, UP*((pack_position+i)%3 -1 )*2.5) for i in range(3)])
            self.wait()
            reordered_packs =[[],[],[]]
            for i in range(3):
                reordered_packs[(pack_position+i)%3] = packs[(choosen_pack+i)%3]
            packs = reordered_packs
            self.cards = [item for pack in packs for item in pack]
            center = Group(*packs[0]).get_center()
            self.play(*[ApplyMethod(Group(*pack).move_to, center) for pack in packs[1:]])
            self.cover.move_to(center)
            self.add(self.cover)
            self.play(Group(*self.cards,self.cover).to_corner,UL)
            self.wait()
        counter = TexMobject("0").scale(1.5).to_edge(UP,buff = 2)
        self.play(Write(counter))
        for i in range(target_position):
            self.play(self.cards[i].move_to, ORIGIN,Transform(counter, TexMobject(str(i+1)).scale(1.5).to_edge(UP,buff = 2)))
        question = TextMobject(r"Ez a k\'arty\'ad?").next_to(counter,UP)
        self.play(Write(question))
        self.wait(2)
        self.play(*[FadeOut(m) for m in self.mobjects])


class Explanation(Scene):
    def setup(self):
        self.cards = [ImageMobject("D:\\AnimatedMath\\manim\\media\\assets\\raster_images\\"+ str(digit) + letter +".png") for  digit in range(2,9) for letter in ["C","D","H","S"]]
        self.cards.pop(len(self.cards)-1)
        perm = [18, 5, 9, 1, 25, 20, 21, 10, 19, 22, 15, 8, 12, 13, 16, 3, 0, 2, 7, 17, 23, 6, 26, 11, 24, 4, 14]
        self.cards = [self.cards[perm[i]].to_corner(UL) for i in range(27)]
        self.cover = ImageMobject("D:\\AnimatedMath\\manim\\media\\assets\\raster_images\\cover.png").to_corner(UL)

    def construct(self):
        current_position = 18
        target_position = 20
        title = TextMobject(r"Magyar\'azat").scale(2)
        group = Group(*self.cards).move_to(ORIGIN)
        surround_choosen = SurroundingRectangle(self.cards[current_position])
        surround_choosen.add_updater(lambda mob: mob.become(SurroundingRectangle(self.cards[current_position])))
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(FadeOut(title))
        self.play(FadeIn(group))
        self.play(ApplyMethod(group.arrange_submobjects, RIGHT, {"buff":-1}))
        self.play(self.cards[current_position].shift, 2*DOWN)
        self.play(ShowCreation(surround_choosen))
        self.play(self.cards[current_position].shift, 2*UP)
        self.wait(0.5)
        
        self.play(*[ApplyMethod(mob.scale,0.25) for mob in self.cards])
        self.wait()

        card_0 = self.cards[0]
        rectangles = [Rectangle(width = card_0.get_width(), height = card_0.get_height(),fill_opacity = 0.5, color = BLUE, fill_color = BLUE).move_to(self.cards[i].get_center()) for i in range(27)]
        rectangles[current_position].set_fill(ORANGE).set_stroke(ORANGE)
        surround_choosen.clear_updaters()
        self.add(surround_choosen)
        self.play(AnimationGroup(*[ShowCreation(rect) for rect in rectangles], lag_ratio = 0.1), AnimationGroup(*[FadeOut(card) for card in self.cards], lag_ratio = 0.1))
        self.play(FadeOut(surround_choosen), run_time =0.5)
        self.play(ApplyMethod(VGroup(*rectangles).to_edge, UP, {"buff":1.5}), run_time = 2)

        grid_rectangles = [r.deepcopy() for r in rectangles]
        for column in range(3):
            for row in range(9):
                grid_rectangles[3*row+column].move_to(4*LEFT+RIGHT*(column-1)+DOWN*0.55*(row-1.5))
        self.play(AnimationGroup(*[ReplacementTransform(source.deepcopy(),dest) for source, dest in zip(rectangles,grid_rectangles)], lag_ratio = 0.8))
        indeces = [TexMobject(str(i)).scale(0.65).set_color(BLUE).next_to(rectangles[i],UP,buff = 0.15) for i in range(27)]
        column_indeces = [TexMobject(str(i)).scale(0.65).next_to(grid_rectangles[i],UP,buff = 0.15) for i in range(3)]
        row_indeces = [TexMobject(str(i)).scale(0.65).next_to(grid_rectangles[3*i], LEFT, buff = 0.3) for i in range(9)]

        indeces[current_position].set_color(ORANGE)
        self.play(Write(VGroup(*indeces,*column_indeces, *row_indeces)))
        X = TexMobject("x", color = GREEN).scale(0.65).next_to(indeces[current_position],UP, 0.2)
        I = TexMobject("i", color = GREEN).scale(0.65).next_to(row_indeces[6],LEFT, 0.2)
        J = TexMobject("j", color = GREEN).scale(0.65).next_to(column_indeces[0],UP, 0.15)
        self.play(Write(VGroup(X,I,J)))
        self.play(*[ShowCreationThenFadeAround(mob) for mob in [X,I,J]])
        equation = TexMobject("x","=","3","i","+","j")
        for i in [0,3,5]:
            equation[i].set_color(GREEN)
        equation.move_to(2*RIGHT)
        self.play(*[Write(equation[i]) for i in [1,2,4]])
        self.wait()
        self.play(*[ReplacementTransform(source.deepcopy(),equation[i]) for source,i in zip([X,I,J],[0,3,5])], run_time = 1.5)
        self.wait()
        equation_0 = TexMobject(r"j",r"\in\{0,1,2\}",r"\Longrightarrow", r"j",r" = x\, (mod\, 3)", tex_to_color_map = {"j":GREEN,"x":GREEN}, background_stroke_width = 0).next_to(equation,DOWN,buff = 0.4)
        self.play(Write(equation_0[:3]))
        self.play(ReplacementTransform(equation_0[0].deepcopy(),equation_0[3]))
        self.play(Write(equation_0[4:]))
        self.wait()
        equation_1 = TexMobject(r"3","i",r"\le"," x ",r"\le","3","i","+","2",tex_to_color_map = {"i":GREEN,"x":GREEN}).next_to(equation_0,DOWN,buff = 0.4)
        self.play(*[Write(equation_1[i]) for i in [2,4,7]])
        self.play(*[ReplacementTransform(equation[i].deepcopy(),equation_1[j]) for i,j in zip([0,2,2,3,3,5],[3,0,5,1,6,8])])
        equation_2 = TexMobject(r"3","i",r"\le"," x ",r"<","3","i","+","3",tex_to_color_map = {"i":GREEN,"x":GREEN}).next_to(equation_0,DOWN,buff = 0.4)
        #                         0   1     2     3     4   5   6   7   8
        self.play(ReplacementTransform(equation_1,equation_2))
        equation_3 = TexMobject("i",r"\le",r" {x\over3} ","<","i","+","1",tex_to_color_map = {"i":GREEN,"x":GREEN}).next_to(equation_0,DOWN,buff = 0.4)
        #                        0     1      23   4       5   6   7   8
        self.play(*[ReplacementTransform(equation_2[i],equation_3[j]) for i,j in [(0,4),(1,0),(2,1),(3,3),(4,5),(5,4),(6,6),(7,7),(8,8)]])
        self.wait()
        equation_4 = TexMobject("i",r"\le",r" {x\over3} ","<","i","+","1",r"\Longrightarrow",r"\left[ {x\over3}\right]=","i",tex_to_color_map = {"x":GREEN}).next_to(equation_0,DOWN,buff = 0.4)
        equation_4[0].set_color(GREEN)
        equation_4[6].set_color(GREEN)
        equation_4[len(equation_4)-1].set_color(GREEN)
        self.play(ReplacementTransform(equation_3[:9],equation_4[:9]))
        self.play(Write(equation_4[9:]))
        equation_5 = TexMobject(r"\left[ {x\over3}\right]=","i",tex_to_color_map = {"x":GREEN}).to_corner(DR,buff = 0.4)
        equation_5[len(equation_5)-1].set_color(GREEN)
        self.wait()
        self.play(ReplacementTransform(equation_4[10:].deepcopy(),equation_5),*[FadeOut(m) for m in [equation,equation_0,equation_4,J]],ApplyMethod(VGroup(*rectangles,*indeces,X).shift,0.5*UP))
        self.wait()
        self.play(ShowCreationThenDestructionAround(VGroup(*[grid_rectangles[3*i] for i in range(9)])))
        self.wait()
        
        permutated_rectangles = [ grid_rectangles[3*i+(j-1)%3].deepcopy().shift((4+a)*RIGHT) for i in range(9) for j,a in zip(range(3),[-2,1,1])]
        #self.play(ShowCreation(VGroup(*permutated_rectangles)))
        for j in range(3):
            self.play(*[ReplacementTransform(grid_rectangles[3*i+j].deepcopy(),permutated_rectangles[3*i+(j+1)%3], path_arc = PI/4) for i in range(9)])
        self.wait()
        Y = TexMobject("y").set_color(RED).next_to(VGroup(*[permutated_rectangles[3*i+1] for i in range(9)]), UP, buff = 0.2).scale(0.65)
        Y9 = TexMobject("9","y",tex_to_color_map = {"y":RED}).scale(0.65).next_to(indeces[9],DOWN,buff = 2.6)
        self.play(Write(Y))
        self.play(ShowCreationThenFadeAround(Y))
        perm_row_indeces = [i.deepcopy() for i in row_indeces]
        I_0 = I.deepcopy()
        self.play(ApplyMethod(VGroup(I_0,*perm_row_indeces).shift,4*RIGHT))
        self.wait()
        for j in range(3):
            if j==1:
                self.play(*[ApplyMethod(permutated_rectangles[3*i+j].next_to,rectangles[9*j+i],DOWN, {"buff":0.3}) for i in range(9)], 
                          *[ApplyMethod(perm_row_indeces[i].next_to,rectangles[9*j+i],DOWN, {"buff":1.3}) for i in range(9)],
                            Write(Y9[0]), Transform(Y,Y9[1]), ApplyMethod(I_0.next_to, indeces[15],DOWN,{"buff":2.6}))        
            else:   
                self.play(*[ApplyMethod(permutated_rectangles[3*i+j].next_to,rectangles[9*j+i],DOWN, {"buff":0.3}) for i in range(9)])
        text_0 = TexMobject(r"\mbox{Az \'uj poz\'\i ci\'o: }", "9","y","+","i").move_to(DOWN+RIGHT)
        for c,i in zip([RED,GREEN],[2,4]):
            text_0[i].set_color(c)
        self.play(Write(text_0[0]),Write(text_0[3]))
        self.play(ReplacementTransform(Y9.deepcopy(), text_0[1:3]), ReplacementTransform(I_0.deepcopy(),text_0[4]))
        self.wait()
        text_1 = TexMobject(r"\mbox{Az \'uj poz\'\i ci\'o: }", "9","y","+",r"\left[ { {x} \over3}\right]",tex_to_color_map = {"y":RED,r"{x}":GREEN}).move_to(DOWN+RIGHT)
        self.play(ReplacementTransform(text_0[:4],text_1[:4]), ReplacementTransform(equation_5,text_1[4:]),FadeOut(text_0[4]))
        self.wait()
        self.play(*[FadeOut(m) for m in [*grid_rectangles,*row_indeces,*perm_row_indeces,Y9,I_0,I,*column_indeces,Y]])
        self.wait()
        self.play(VGroup(*permutated_rectangles).shift, DOWN)
        self.wait()
        dot = Dot()
        position_function_0 = TexMobject(r"x_1=9y_0 + \left[{x_0\over3}\right]",tex_to_color_map = {"y_0":RED,"x_0":GREEN,"x_1":GREEN}).scale(0.65).to_edge(RIGHT,buff = 1).shift(2*UP)
        position_function_1 = TexMobject(r"x_2=9y_1 + \left[{x_1\over3}\right]",tex_to_color_map = {"y_1":RED,"x_1":GREEN,"x_2":GREEN}).scale(0.65).to_edge(RIGHT,buff = 1)
        position_function_2 = TexMobject(r"x_3=9y_2 + \left[{x_2\over3}\right]",tex_to_color_map = {"y_2":RED,"x_2":GREEN,"x_3":GREEN}).scale(0.65).to_edge(RIGHT,buff = 1).shift(2*DOWN)
        X0 = TexMobject("x_0").move_to(X.get_center()).scale(0.65).set_color(GREEN)
        Y0 = TextMobject(r"Els\H o oszt\'asn\'al $y_0$\,$=1$.",tex_to_color_map = {"$y_0$":RED}).scale(0.65).to_edge(LEFT,buff = 0.2).shift(2*UP)
        Y1 = TextMobject(r"M\'asodik oszt\'asn\'al $y_1$\,$=0$.",tex_to_color_map = {"$y_1$":RED}).scale(0.65).to_edge(LEFT,buff = 0.2)
        Y2 = TextMobject(r"Harmadik oszt\'asn\'al $y_2$\,$=2$.",tex_to_color_map = {"$y_2$":RED}).scale(0.65).to_edge(LEFT,buff = 0.2).shift(2*DOWN)
        X1 = TexMobject("x_1").scale(0.65).next_to(rectangles[15],DOWN,buff = 1).set_color(GREEN)
       
        pos0 = dot.next_to(rectangles[18],DOWN, buff = 0.2).get_center()
        pos1 = dot.next_to(rectangles[15],DOWN,buff = 1).get_center()
        arrow0 = Arrow(pos0,pos1).scale_in_place(0.8)
        
        X2 = TexMobject("x_2").scale(0.65).set_color(GREEN)
        X3 = TexMobject("x_3").scale(0.65).set_color(GREEN)
        
        self.play(AnimationGroup(Write(Y0),Transform(X,X0),Write(X1),ShowCreation(arrow0),ReplacementTransform(text_1,position_function_0),lag_ratio = 0.9))
        self.wait()
        
        rectangles_1 = [r.deepcopy().shift(3.6*DOWN) for r in rectangles]
        pos = rectangles_1[18].get_center()
        rectangles_1[18].move_to(rectangles_1[5].get_center())
        rectangles_1[5].move_to(pos)
        rectangles_1[5],rectangles_1[18] =  rectangles_1[18],rectangles_1[5] 
        X2.next_to(rectangles_1[5],UP,buff = 0.2)

        pos0 = dot.next_to(rectangles_1[15],UP, buff = 1).get_center()
        pos1 = dot.next_to(rectangles_1[5],UP,buff = 0.2).get_center()
        arrow1 = Arrow(pos0,pos1).scale_in_place(0.8)

        self.play(ShowCreation(VGroup(*rectangles_1)))
        self.play(AnimationGroup(*[Write(m) for m in [Y1,X2,arrow1,position_function_1]], lag_ratio = 0.9))
        self.wait()

        rectangles_2 = [r.deepcopy().shift(5.6*DOWN) for r in rectangles]
        pos = rectangles_2[18].get_center()
        rectangles_2[18].move_to(rectangles_2[19].get_center())
        rectangles_2[19].move_to(pos)
        rectangles_2[18],rectangles_2[19] =  rectangles_2[19],rectangles_2[18] 
        X3.next_to(rectangles_2[19],UP,buff = 0.2)

        pos0 = dot.next_to(rectangles_1[5],DOWN, buff = 0.2).get_center()
        pos1 = dot.next_to(rectangles_2[19],UP,buff = 0.2).get_center()
        arrow2 = Arrow(pos0,pos1).scale_in_place(0.8)

        positions = [TexMobject(str(i)).scale(0.65).set_color(BLUE).next_to(rectangles_2[i-1],DOWN,buff = 0.2) for i in range(1,28)]
        positions[19].set_color(ORANGE)
        self.play(ShowCreation(VGroup(*rectangles_2)))
        self.play(AnimationGroup(*[Write(m) for m in [Y2,X3,arrow2,position_function_2,VGroup(*positions)]], lag_ratio = 0.9))
        
        self.play(ShowCreationThenFadeAround(positions[19]), run_time = 1.5)
        self.wait()
        
        eq_group = VGroup(position_function_0,position_function_1,position_function_2)
        question = TextMobject(r"Az $y_0$, $y_1$, $y_2$ sz\'amok meghat\'aroz\'as\'aban rejlik a tr\"ukk!",tex_to_color_map = {"$y_0$":RED,"$y_2$":RED,"$y_1$":RED} )
        self.play(*[FadeOutAndShiftDown(m) for m in [*rectangles_1,*permutated_rectangles,arrow0,arrow1,arrow2,X1,X2,Y0,Y1,Y2]],
                ApplyMethod(eq_group.arrange_submobjects,RIGHT,{"buff":1}))
        self.play(ApplyMethod(eq_group.shift, 1.5*UP))
        self.play(Write(question))
        self.wait(2)
        equation_6 = TexMobject("x_3 ="," 9","y_2 + ",r"\left[{",r"x_2\over3",r"}\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"x_2":GREEN})
        equation_7 = TexMobject("x_3 ="," 9","y_2 + ",r"\left[",r"{1\over3}\left(9y_1+\left[{x_1\over3}\right]\right)",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"x_1":GREEN})
        equation_8 = TexMobject("x_3 ="," 9","y_2 + ","3y_1 + ",r"\left[",r"{1\over3}\left[{x_1\over3}\right]",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"x_1":GREEN})
        equation_9 = TexMobject("x_3 ="," 9","y_2 + ","3y_1 + ",r"\left[",r"{x_1\over9}",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"x_1":GREEN})
        equation_10 = TexMobject("x_3 ="," 9","y_2 + ","3y_1 + ",r"\left[",r"{1\over9}\left(9y_0+\left[{x_0\over3}\right]\right)",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"y_0":RED,"x_0":GREEN})
        equation_11 = TexMobject("x_3 ="," 9","y_2 + ","3y_1 + ","y_0+",r" \left[",r"{1\over9}\left[{x_0\over3}\right]",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"y_0":RED,"x_0":GREEN})
        equation_12 = TexMobject("x_3","="," 9","y_2","+","3","y_1 ","+","y_0","+",r" \left[",r"{x_0\over27}",r"\right]",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"y_0":RED,"x_0":GREEN})
        equation_13 = TexMobject("x_3","=","3^2","y_2","+","3^1","y_1","+3^0","y_0",tex_to_color_map= {"x_3":GREEN,"y_2":RED,"y_1":RED,"y_0":RED})
        equation_reason = TexMobject(r"\left[{[x]\over n}\right] = \left[{x\over n}\right],\forall n\in\mathbb{N}^*,\forall x\in\mathbb{R}").scale(0.65)
        self.play(FadeOut(question))
        self.play(ReplacementTransform(position_function_2,equation_6))
        self.play(FocusOn(equation_6[6]))
        self.play(ShowCreationThenFadeAround(position_function_1))
        self.wait(0.5)
        self.play(FadeOut(position_function_1),ReplacementTransform(equation_6[:3],equation_7[:3]),
                  ReplacementTransform(equation_6[3],equation_7[3]),
                  ReplacementTransform(equation_6[4: len(equation_6)-1],equation_7[4:len(equation_7)-1]),
                  ReplacementTransform(equation_6[len(equation_6)-1],equation_7[len(equation_7)-1]))
        self.wait(0.5)
        self.play(ReplacementTransform(equation_7[:5],equation_8[:5]),ReplacementTransform(equation_7[5:7],equation_8[5:8]), ReplacementTransform(equation_7[7:],equation_8[8:]))
        self.wait(0.5)
        equation_reason.next_to(position_function_0,RIGHT,buff = 1)
        self.play(FadeIn(equation_reason))
        self.wait()
        self.play(Indicate(equation_8[8:]))
        self.wait(0.5)
        self.play(ShowCreationThenFadeAround(equation_reason))
        self.wait(0.5)
        self.play(ReplacementTransform(equation_8[:8],equation_9[:8]),ReplacementTransform(equation_8[8:],equation_9[8:]) )
        

        self.play(FocusOn(equation_9[10]))
        self.wait(0.5)
        self.play(ShowCreationThenFadeAround(position_function_0))
        self.wait(0.5)
        self.play(FadeOut(position_function_0),ReplacementTransform(equation_9[:9],equation_10[:9]), ReplacementTransform(equation_9[9:],equation_10[9:]),equation_reason.shift, equation_reason.get_center()[0]*LEFT)
        self.wait(0.5)
        self.play(ReplacementTransform(equation_10[:9],equation_11[:9]),ReplacementTransform(equation_10[9:13],equation_11[9:12]),ReplacementTransform(equation_10[13:],equation_11[12:]) )
        self.play(Indicate(equation_11[10:]))
        self.wait(0.5)
        self.play(ShowCreationThenFadeAround(equation_reason))
        self.wait(0.5)
        self.play(ReplacementTransform(equation_11[:10],equation_12[:10]),ReplacementTransform(equation_11[10:],equation_12[10:]),FadeOut(equation_reason))
        self.wait()
        #insert reason
        small_enough = TexMobject(r"0\le x_0 < ","27", r"\Longrightarrow", r"0\le {x_0\over 27}","<","1", r"\Longrightarrow", r"\left[{x_0\over 27}",r"\right]","=","0",
        background_stroke_width = 0, tex_to_color_map = {"x_0":GREEN}).shift(1.5*UP)
        #                           0     1  2     3           4                5    6    7       8   9          10                 11  12    13        14    15  16
        self.play(AnimationGroup(Write(small_enough[:4]),Write(small_enough[4]), lag_ratio = 1.5))
        self.play(*[Write(small_enough[i]) for i in [5,8]])
        self.play(AnimationGroup(*[ReplacementTransform(small_enough[i].deepcopy(),small_enough[j],path_arc = PI/4) for i,j in [(1,6),(3,7),(3,9)]],lag_ratio = 0.8))
        self.play(AnimationGroup(Write(small_enough[10]),Write(VGroup(*[small_enough[i] for i in [11,14,15,16]])),lag_ratio = 1.5))
        self.play(*[ReplacementTransform(small_enough[i].deepcopy(),small_enough[j], path_arc = PI/4) for i,j in [(6,12),(7,13)]])
        self.wait()
        self.play(Indicate(equation_12[9:]))
        self.wait(0.5)
        self.play(FocusOn(small_enough[11:]))
        self.wait(0.5)
        self.play(*[ReplacementTransform(equation_12[i],equation_13[i]) for i in range(9)],FadeOut(equation_12[9:]),FadeOut(small_enough))
        self.play(equation_13.shift,1.5*UP)
        text_2 = TextMobject(r"Teh\'at $y_0$, $y_1$, $y_2$ nem m\'as mint az $x_3$\\ h\'armas sz\'amredszerbeli alakj\'anak a sz\'amjegyei.",tex_to_color_map = {"$y_0$":RED,"$y_2$":RED,"$y_1$":RED, "$x_3$":GREEN})
        self.play(Write(text_2),run_time = 3)
        self.wait(2.5)
        text_3 = TextMobject(r"Tr\"ukk v\'egrehajt\'asa")
        self.play(ReplacementTransform(text_2,text_3))
        self.wait(2)
        text_4 = TextMobject(r"Kever\'es ut\'an k\'er\"unk egy $n$ sz\'amot, amelyre $1\le$\, $n$\, $\le27$", tex_to_color_map={"$n$":ORANGE})
        self.wait(3.5)
        self.play(ReplacementTransform(text_3,text_4))
        equation_Y = TexMobject(r"n-1 = (y_2y_1y_0)_3", tex_to_color_map={"n":ORANGE,"y_0":RED,"y_2":RED,"y_1":RED})
        equation_Y.next_to(text_4,DOWN,buff = 0.8)
        self.wait(2)
        self.play(Write(equation_Y))
        self.wait()
        self.play(FadeOut(equation_13),ApplyMethod(equation_Y.move_to, equation_13.get_center()))
        text_5 = TextMobject(r"Az $i$-k leoszt\'asn\'al a megjel\"olt csom\'ot az $y_i$-ikk\'ent vessz\"uk fel,\\ majd lappal lefele ford\'\i tjuk az \"osszeszedett csom\'ot.",
                                 tex_to_color_map = {"$y_i$":RED,r"megjel\"olt":YELLOW})
        self.play(FadeOut(text_4))
        self.play(Write(text_5,run_time = 2))
        self.wait(3.5)
        text_6 = TextMobject(r"A $3$ felszed\'es ut\'an a csom\'o tetej\'er\H ol lesz\'amolunk $n$ lapot,\\ \'es az utols\'o amit leraktunk a h\'uzott k\'artya.",tex_to_color_map = {"$n$":ORANGE} )
        self.play(FadeOut(equation_Y),FadeOut(text_5))
        self.play(Write(text_6),run_time = 4)
        self.wait(2.5)
        self.play(*[FadeOut(m) for m in [text_6,*rectangles,*rectangles_2, *indeces, *positions,X,X3]])