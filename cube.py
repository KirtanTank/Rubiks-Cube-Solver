from vpython import *
import numpy as np
import random
from solve_rubiccs_cube import *
# from ColorDetection import detect as dt
# from CubeMap import cube_map as cm
# import cv2


class Rubic_Cube:
    def __init__(self, color_dict):
        self.running = True
        self.color_dict = {}
        self.tiles = []
        self.dA = np.pi / 40
        self.color_dict = color_dict
        self.canvas1 = canvas(width=1520, height=550)
        self.canvas1.autoscale = False
        sphere(canvas=self.canvas1, pos=vector(0, 0, 0), size=vector(100, 100, 100), texture='space_background.jpg',
               shininess=0, radius=100)
        # Label
        self.solution_label = label(canvas=self.canvas1, pos=vector(0, 4, 0), color=color.white, box=False, text='',
                                    font='cursive', height=25)
        self.solution_label.visible = False
        # slider for rate
        self.sl = slider(canvas=self.canvas1, min=5, max=100, length=1100, value=60, bind=self.sl_rate)
        self.canvas1.append_to_caption('\t\t')
        self.sl_value_text = wtext(canvas=self.canvas1, text='Moving Rate=' + str(self.sl.value), bind=self.sl_rate)
        self.new_rate = int(self.sl.value)
        self.canvas1.append_to_caption('\n')
        # center
        sphere(canvas=self.canvas1, pos=vector(0, 0, 0), size=vector(3, 3, 3), color=vector(0, 0, 0))
        tile_pos = [
            [vector(-1, 1, 1.5), vector(0, 1, 1.5), vector(1, 1, 1.5),  # front(RED)
             vector(-1, 0, 1.5), vector(0, 0, 1.5), vector(1, 0, 1.5),
             vector(-1, -1, 1.5), vector(0, -1, 1.5), vector(1, -1, 1.5), ],

            [vector(1.5, 1, 1), vector(1.5, 1, 0), vector(1.5, 1, -1),  # right(YELLOW)
             vector(1.5, 0, 1), vector(1.5, 0, 0), vector(1.5, 0, -1),
             vector(1.5, -1, 1), vector(1.5, -1, 0), vector(1.5, -1, -1), ],

            [vector(1, 1, -1.5), vector(0, 1, -1.5), vector(-1, 1, -1.5),  # back(ORANGE)
             vector(1, 0, -1.5), vector(0, 0, -1.5), vector(-1, 0, -1.5),
             vector(1, -1, -1.5), vector(0, -1, -1.5), vector(-1, -1, -1.5), ],

            [vector(-1.5, 1, -1), vector(-1.5, 1, 0), vector(-1.5, 1, 1),  # left(WHITE)
             vector(-1.5, 0, -1), vector(-1.5, 0, 0), vector(-1.5, 0, 1),
             vector(-1.5, -1, -1), vector(-1.5, -1, 0), vector(-1.5, -1, 1), ],

            [vector(-1, 1.5, -1), vector(0, 1.5, -1), vector(1, 1.5, -1),  # top(BLUE)
             vector(-1, 1.5, 0), vector(0, 1.5, 0), vector(1, 1.5, 0),
             vector(-1, 1.5, 1), vector(0, 1.5, 1), vector(1, 1.5, 1), ],

            [vector(-1, -1.5, 1), vector(0, -1.5, 1), vector(1, -1.5, 1),  # bottom(GREEN)
             vector(-1, -1.5, 0), vector(0, -1.5, 0), vector(1, -1.5, 0),
             vector(-1, -1.5, -1), vector(0, -1.5, -1), vector(1, -1.5, -1), ],
        ]

        color_choose = self.color_dict

        for i in color_choose.copy():
            # print(i)
            list_values = color_choose[i]
            for j in range(len(list_values)):
                print(list_values[j])
                if list_values[j] == "R":
                    del list_values[j]
                    list_values.insert(j, vector(1, 0, 0))
                elif list_values[j] == "Y":
                    del list_values[j]
                    list_values.insert(j, vector(1, 1, 0))
                elif list_values[j] == "O":
                    del list_values[j]
                    list_values.insert(j, vector(1, 0.5, 0))
                elif list_values[j] == "W":
                    del list_values[j]
                    list_values.insert(j, vector(1, 1, 1))
                elif list_values[j] == "B":
                    del list_values[j]
                    list_values.insert(j, vector(0, 0, 1))
                else:
                    del list_values[j]
                    list_values.insert(j, vector(0, 1, 0))

        print("color_choose: ", color_choose)

        # Face color
        colors = []
        for i in color_choose:
            for j in color_choose[i]:
                colors.append(j)

        print("colors: ", colors)

        angle = [(0, vector(0, 0, 0)), (np.pi / 2, vector(0, 1, 0)), (0, vector(0, 0, 0)), (np.pi / 2, vector(0, 1, 0)),
                 (np.pi / 2, vector(1, 0, 0)), (np.pi / 2, vector(1, 0, 0))]

        # sides
        i = 0
        for rank, side in enumerate(tile_pos):
            print("rank: ", rank, " ", "side: ", side)
            for vec in side:
                print("vec: ", vec)
                tile = box(canvas=self.canvas1, pos=vec, size=vector(0.98, 0.98, 0.1), color=colors[i])
                tile.rotate(angle=angle[rank][0], axis=angle[rank][1])
                self.tiles.append(tile)
                i += 1
                print("pos:", tile.pos, " ", "color: ", tile.color)

        print("tiles: ", self.tiles)

        # positions
        self.positions = {'front': [], 'right': [], 'back': [], 'left': [], 'top': [], 'bottom': []}

        # variables
        self.rotate = [None, 0, 0]
        self.moves = []

    def reset_positions(self):
        self.positions = {'front': [], 'right': [], 'back': [], 'left': [], 'top': [], 'bottom': []}
        for tile in self.tiles:
            if tile.pos.z > 0.4:
                self.positions['front'].append(tile)
            if tile.pos.x > 0.4:
                self.positions['right'].append(tile)
            if tile.pos.z < -0.4:
                self.positions['back'].append(tile)
            if tile.pos.x < -0.4:
                self.positions['left'].append(tile)
            if tile.pos.y > 0.4:
                self.positions['top'].append(tile)
            if tile.pos.y < -0.4:
                self.positions['bottom'].append(tile)

        for key in self.positions.keys():
            self.positions[key] = set(self.positions[key])

    def animations(self):
        if self.rotate[0] == 'front_counter':
            pieces = self.positions['front']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'right_counter':
            pieces = self.positions['right']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'back_counter':
            pieces = self.positions['back']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(0, 0, -1), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'left_counter':
            pieces = self.positions['left']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(-1, 0, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'top_counter':
            pieces = self.positions['top']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'bottom_counter':
            pieces = self.positions['bottom']
            for tile in pieces:
                tile.rotate(angle=self.dA, axis=vector(0, -1, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'front_clock':
            pieces = self.positions['front']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(0, 0, 1), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'right_clock':
            pieces = self.positions['right']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(1, 0, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'back_clock':
            pieces = self.positions['back']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(0, 0, -1), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'left_clock':
            pieces = self.positions['left']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(-1, 0, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'top_clock':
            pieces = self.positions['top']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(0, 1, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        elif self.rotate[0] == 'bottom_clock':
            pieces = self.positions['bottom']
            for tile in pieces:
                tile.rotate(angle=(-self.dA), axis=vector(0, -1, 0), origin=vector(0, 0, 0))
            self.rotate[1] += self.dA
        if self.rotate[1] + self.dA / 2 > self.rotate[2] > self.rotate[1] - self.dA / 2:
            self.rotate = [None, 0, 0]
            self.reset_positions()

    def rotate_front_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['front_counter', 0, np.pi / 2]

    def rotate_right_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['right_counter', 0, np.pi / 2]

    def rotate_back_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['back_counter', 0, np.pi / 2]

    def rotate_left_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['left_counter', 0, np.pi / 2]

    def rotate_top_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['top_counter', 0, np.pi / 2]

    def rotate_bottom_counter(self):
        if self.rotate[0] is None:
            self.rotate = ['bottom_counter', 0, np.pi / 2]

    def rotate_front_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['front_clock', 0, np.pi / 2]

    def rotate_right_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['right_clock', 0, np.pi / 2]

    def rotate_back_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['back_clock', 0, np.pi / 2]

    def rotate_left_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['left_clock', 0, np.pi / 2]

    def rotate_top_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['top_clock', 0, np.pi / 2]

    def rotate_bottom_clock(self):
        if self.rotate[0] is None:
            self.rotate = ['bottom_clock', 0, np.pi / 2]

    def move(self):
        possible_moves = ["F", "R", "B", "L", "U", "D", "F'", "R'", "B'", "L'", "U'", "D'"]
        if self.rotate[0] is None and len(self.moves) > 0:
            if self.moves[0] == possible_moves[0]:
                self.rotate_front_clock()
            elif self.moves[0] == possible_moves[1]:
                self.rotate_right_clock()
            elif self.moves[0] == possible_moves[2]:
                self.rotate_back_clock()
            elif self.moves[0] == possible_moves[3]:
                self.rotate_left_clock()
            elif self.moves[0] == possible_moves[4]:
                self.rotate_top_clock()
            elif self.moves[0] == possible_moves[5]:
                self.rotate_bottom_clock()
            elif self.moves[0] == possible_moves[6]:
                self.rotate_front_counter()
            elif self.moves[0] == possible_moves[7]:
                self.rotate_right_counter()
            elif self.moves[0] == possible_moves[8]:
                self.rotate_back_counter()
            elif self.moves[0] == possible_moves[9]:
                self.rotate_left_counter()
            elif self.moves[0] == possible_moves[10]:
                self.rotate_top_counter()
            elif self.moves[0] == possible_moves[11]:
                self.rotate_bottom_counter()
            self.moves.pop(0)

    def scramble(self):
        self.solution_label.visible = False
        self.solution_label.text = ''
        possible_moves = ["F", "R", "B", "L", "U", "D", "F'", "R'", "B'", "L'", "U'", "D'", "F2", "R2", "B2", "L2", "U2"
            , "D2"]
        for i in range(35):
            self.moves.append(random.choice(possible_moves))

    def solution(self):
        solution_text = solve(self.tiles)
        self.solution_label.visible = True
        self.solution_label.text = f"\nSolution: {solution_text}"
        return solution_text

    def solve(self):
        values = solve(self.tiles)
        values = list(values.split(" "))
        print("values in solve fun in cube.py: ", values)
        for value in values:
            lis_value = list(value)
            if lis_value[-1] == '2':
                lis_value.pop(-1)
                value = ''.join(lis_value)
                self.moves.append(value)
                self.moves.append(value)
            else:
                self.moves.append(value)

    def sl_rate(self):
        new_sl = self.sl
        sl_value = self.sl_value_text
        self.new_rate = int(new_sl.value)
        sl_value.text = '<b style="font-size:20px;font-family:cursive">Moving Rate=</b>' + str(self.new_rate)
        return self.new_rate

    # def restart_process(self):
    #     restart_process_new(self.color_dict)

    def control(self):
        self.canvas1.append_to_caption('\n')
        self.canvas1.append_to_caption('\t\t')
        button(bind=self.solution, text='<b><h1 style="font-size:15px;font-family:cursive">Solution</b>',
               canvas=self.canvas1, background=color.blue, color=color.white)
        self.canvas1.append_to_caption('\t\t\t\t\t\t\t\t')

        button(bind=self.solve, text='<b><h1 style="font-size:15px;font-family:cursive">Solve It!</b>',
               canvas=self.canvas1, background=color.blue, color=color.white)
        self.canvas1.append_to_caption('                           \t\t\t\t\t')

        button(bind=self.scramble, text='<b><h1 style="font-size:15px;font-family:cursive">Scramble</b>',
               canvas=self.canvas1, background=color.blue, color=color.white)
        self.canvas1.append_to_caption('\t\t\t\t\t\t\t\t')

        # button(bind=self.restart_process, text='<b><h1 style="font-size:15px;font-family:cursive">Restart</b>',
        #        canvas=self.canvas1, background=color.blue, color=color.white)

        self.canvas1.append_to_caption('\n\n')
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_front_clock, text='<b><h1 style="font-size:15px;font-family:cursive">     F     '
                                                  '</h1></b>', canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_front_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    F'    "
                                                    "</h1></b>",
               canvas=self.canvas1, background=color.blue, color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_right_clock, text='<b><h1 style="font-size:15px;font-family:cursive">     R     '
                                                  '</h1></b>', canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_right_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    R'    "
                                                    "</h1></b>", canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_back_clock, text='<b><h1 style="font-size:15px;font-family:cursive">     B     '
                                                 '</h1></b>', canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_back_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    B'    "
                                                   "</h1></b>", canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_left_clock, text='<b><h1 style="font-size:15px;font-family:cursive">     L     '
                                                 '</h1></b>', canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_left_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    L'    "
                                                   "</h1></b>", canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_top_clock,
               text='<b><h1 style="font-size:15px;font-family:cursive">     U     </h1></b>',
               canvas=self.canvas1, background=color.blue, color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_top_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    U'    "
                                                  "</h1></b>", canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_bottom_clock, text='<b><h1 style="font-size:15px;font-family:cursive">     D     '
                                                   '</h1></b>', canvas=self.canvas1, background=color.blue,
               color=color.white)
        self.canvas1.append_to_caption('\t')
        button(bind=self.rotate_bottom_counter, text="<b><h1 style=\"font-size:15px;font-family:cursive\">    D'    "
                                                     "</h1></b>", canvas=self.canvas1, background=color.blue,
               color=color.white)

    def update(self):
        rate(self.sl_rate())
        self.animations()
        self.move()

    def start(self):
        self.reset_positions()
        self.control()
        while self.running:
            self.update()

#
# def restart_process_new(color_dict):
#     for i in range(6):
#         y = dt()
#         center = y[4]
#         color_dict[center] = y
#
#     cv2.destroyAllWindows()
#     cm(color_dict)
#     cube = Rubic_Cube(color_dict)
#     cube.start()
