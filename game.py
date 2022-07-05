from functools import total_ordering
import random
from colorama import init, Fore, Back, Style
import numpy as np
from colorama import init as cinit
import sys
import termios
import tty
import signal
import os
import sys
import termios
import tty
import time
# from time import sleep, time
from math import pi
from input import input_to, Get
str_tme = []
builds_str = []
height = 30
width = 100
Total = 0
screen = [[' ' for x in range(0, width)]
          for y in range(0, height)]

build_pres = [[' ' for x in range(0, width)]
              for y in range(0, height)]

trp_cnt = [0, 0, 0]
level = [1]
cannons = []
wizt = []
huts = []

limit = [8, 6, 4]
file = open(f"replays/{len(os.listdir('./replays')) + 1}.txt", "w")
val = input("Press 1 to use King and 0 to use Queen as troop : ")
file.write(val)
file.write('\n')

class Screen(object):
    """Class to handle screen."""

    def __init__(self, height, width, screen):
        self.height = height
        self.width = width
        self.screen = screen

    def draw(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                if(self.screen[y][x] == Fore.LIGHTCYAN_EX + "K" and val == "0"):
                    print(Fore.LIGHTCYAN_EX + "Q", end='')
                else:
                    print(Fore.BLUE + self.screen[y][x], end='')
            print()


list_of_buildings = []


class Buildings(object):
    def __init__(self, board, bpos, name, height, width, TLx, TLy, shape):
        self.board = board
        self.status = True
        self.bpos = bpos
        self.range = 6
        self.damage = 25
        self.height = height
        self.width = width
        self.name = name
        self.TLx = TLx
        self.TLy = TLy
        self.shape = shape
        self.health = 100
        self.buildings = [[" " for y in range(self.height)]
                          for x in range(self.width)]
        list_of_buildings.append(self)
        global Total
        Total = Total + 1

    def render(self):

        if self.health > 0:
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = self.shape
                    self.bpos.screen[self.TLy + y][self.TLx + x] = self.name
        else:
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = ' '
                    self.bpos.screen[self.TLy + y][self.TLx + x] = ' '

    def girgit(self):
        global Total
        if self.name[0] == 'c':
            self.shape = 'c'
        if self.name[0] == 'h':
            self.shape = 'h'
        if self.name[0] == 'w':
            self.shape = 'w'
        if(self.health <= 100 and self.health > 50):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTGREEN_EX + self.shape
        if(self.health <= 50 and self.health > 20):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTYELLOW_EX + self.shape
        if(self.health <= 20 and self.health > 0):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTRED_EX + self.shape
        if(self.health <= 0):
            self.status = False
            Total = Total - 1
            self.health = 0
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = ' '
                    self.bpos.screen[self.TLy + y][self.TLx + x] = ' '

    def girgeet(self):
        global Total
        self.shape = '&'
        if(self.health > 100 and self.health <= 200):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTGREEN_EX + self.shape
        if(self.health <= 100 and self.health > 60):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTYELLOW_EX + self.shape
        if(self.health <= 60 and self.health > 0):
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = Fore.LIGHTRED_EX + self.shape
        if(self.health <= 0):
            self.status = False
            Total = Total - 1
            self.health = 0
            for y in range(self.height):
                for x in range(self.width):
                    self.board.screen[self.TLy +
                                      y][self.TLx + x] = ' '
                    self.bpos.screen[self.TLy + y][self.TLx + x] = ' '


class Cannon(Buildings):
    def attack(self):
        flag = False
        # for King
        dist1 = abs(king.x - self.TLx) + abs(king.y - self.TLy)
        if (dist1 <= self.range and self.health > 0 and king.health > 0 and flag == False):
            os.system('aplay -q cannon.wav&')
            king.health = king.health - i.damage
            flag = True
        for j in bian_list:
            dist = abs(self.TLx - j.x) + abs(self.TLy - j.y)
            if(dist <= self.range and self.health > 0 and j.health > 0 and flag == False):
                os.system('aplay -q cannon.wav&')
                j.health = j.health - self.damage
                flag = True
        if not flag:
            for j in arch_list:
                dist = abs(self.TLx - j.x) + abs(self.TLy - j.y)
                if(dist <= self.range and self.health > 0 and j.health > 0 and flag == False):
                    os.system('aplay -q cannon.wav&')
                    j.health = j.health - self.damage
                    flag = True


class WizTower(Buildings):
    def attack(self):
        flag = False
        # for King
        dist1 = abs(king.x - self.TLx) + abs(king.y - self.TLy)
        if (dist1 <= self.range and self.health > 0 and king.health > 0 and flag == False):
            os.system('aplay -q cannon.wav&')
            king.health = king.health - self.damage
            flag = True
        attack_pos = []
        for j in bian_list:
            dist = abs(self.TLx - j.x) + abs(self.TLy - j.y)
            if(dist <= self.range and self.health > 0 and j.health > 0 and flag == False):
                os.system('aplay -q cannon.wav&')
                # j.health = j.health - self.damage
                flag = True
                attack_pos.append(j.x)
                attack_pos.append(j.y)
        if not flag:
            for j in arch_list:
                dist = abs(self.TLx - j.x) + abs(self.TLy - j.y)
                if(dist <= self.range and self.health > 0 and j.health > 0 and flag == False):
                    os.system('aplay -q cannon.wav&')
                    # j.health = j.health - self.damage
                    flag = True
                    attack_pos.append(j.x)
                    attack_pos.append(j.y)
        if not flag:
            for z in loon_list:
                dist = abs(self.TLx - z.x) + abs(self.TLy - z.y)
                if(dist <= self.range and self.health > 0 and z.health > 0 and flag == False):
                    os.system('aplay -q cannon.wav&')
                    # j.health = j.health - self.damage
                    flag = True
                    attack_pos.append(z.x)
                    attack_pos.append(z.y)
        if len(attack_pos) > 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    for barb in bian_list:
                        if barb.x == attack_pos[0] + i and barb.y == attack_pos[1] + j:
                            barb.health -= self.damage
                    for arch in arch_list:
                        if arch.x == attack_pos[0] + i and arch.y == attack_pos[1] + j:
                            arch.health -= self.damage
                    for loon in loon_list:
                        if loon.x == attack_pos[0] + i and loon.y == attack_pos[1] + j:
                            loon.health -= self.damage


class King(object):

    def __init__(self, board, name, x, y, shape):
        self.name = "King"
        self.health = 200
        self.damage = 30
        self.speed = 1
        self.x = x
        self.y = y
        self.shape = shape
        self.board = board

    def rage(self):
        self.damage = self.damage*2
        self.speed = self.speed*2

    def render(self):
        if self.health > 0:
            self.board.screen[self.y][self.x] = self.shape
        else:
            self.board.screen[self.y][self.x] = " "

    def heal(self):
        self.health = min(self.health*1.50, 200)

class Barbarian(object):

    def __init__(self, board, bpos, x, y, shape):
        self.health = 100
        self.damage = 20
        self.speed = 1
        self.x = x
        self.y = y
        self.shape = shape
        self.board = board
        self.bpos = bpos

    def rage(self):
        self.damage = self.damage*2
        self.speed = self.speed*2

    def render(self):
        if self.health > 0:
            self.board.screen[self.y][self.x] = self.shape
            self.bpos.screen[self.y][self.x] = 'B'
        else:
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '

    def heal(self):
        self.health = min(self.health * 1.50, 100)

    def check(self):
        if self.health <= 0:
            self.shape = ' '
            self.health = 0
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '
        if self.health <= 50 and self.health > 0:
            # self.shape = '^' + Fore.LIGHTMAGENTA_EX
            self.board.screen[self.y][self.x] = self.shape
        if self.health > 50 and self.health <= 100:
            self.shape = Fore.MAGENTA + '^'
            self.board.screen[self.y][self.x] = self.shape

    def move(self):
        self.board.screen[self.y][self.x] = ' '
        self.bpos.screen[self.y][self.x] = ' '
        min_distance = np.Inf
        for i in list_of_buildings:
            if i.health > 0:
                for j in range(i.width):
                    for k in range(i.height):
                        # checking manhattan distance of barbs from every point of the building and finding the minimum
                        if abs(i.TLx + j - self.x) + abs(i.TLy + k - self.y) < min_distance:
                            min_distance = abs(
                                i.TLx + j - self.x) + abs(i.TLy + k - self.y)
                            building_to_attack = i
                            final_pos = [i.TLx + j, i.TLy + k]
        if min_distance != np.Inf:
            # keeping range of barbs as 2 and checking that they don't overlap the building
            if min_distance == 1 or (min_distance == 2 and self.x != final_pos[0] and self.y != final_pos[1]):
                if(self.health > 0):
                    building_to_attack.health = building_to_attack.health - self.damage
            else:
                if self.x < final_pos[0]:
                    self.x = self.x + 1
                elif self.x > final_pos[0]:
                    self.x = self.x - 1
                if self.y < final_pos[1]:
                    self.y = self.y + 1
                elif self.y > final_pos[1]:
                    self.y = self.y - 1
        self.board.screen[self.y][self.x] = self.shape
        self.bpos.screen[self.y][self.x] = 'B'


class Loons(object):

    def __init__(self, board, bpos, x, y, shape):
        self.health = 100
        self.damage = 40
        self.speed = 2
        self.x = x
        self.y = y
        self.shape = shape
        self.board = board
        self.bpos = bpos

    def rage(self):
        self.damage = self.damage*2
        self.speed = self.speed*2

    def render(self):
        if self.health > 0:
            self.board.screen[self.y][self.x] = self.shape
            self.bpos.screen[self.y][self.x] = 'L'
        else:
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '

    def heal(self):
        self.health = min(self.health * 1.50, 100)

    def check(self):
        if self.health <= 0:
            self.shape = ' '
            self.health = 0
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '

    def move(self):
        self.board.screen[self.y][self.x] = ' '
        self.bpos.screen[self.y][self.x] = ' '
        min_distance = np.Inf
        for i in cannons:
            if i.health > 0:
                for j in range(i.width):
                    for k in range(i.height):
                        if abs(i.TLx + j - self.x) + abs(i.TLy + k - self.y) < min_distance:
                            min_distance = abs(
                                i.TLx + j - self.x) + abs(i.TLy + k - self.y)
                            building_to_attack = i
                            final_pos = [i.TLx + j, i.TLy + k]
        for i in wizt:
            if i.health > 0:
                for j in range(i.width):
                    for k in range(i.height):
                        if abs(i.TLx + j - self.x) + abs(i.TLy + k - self.y) < min_distance:
                            min_distance = abs(
                                i.TLx + j - self.x) + abs(i.TLy + k - self.y)
                            building_to_attack = i
                            final_pos = [i.TLx + j, i.TLy + k]
        if min_distance == np.Inf:
            for i in list_of_buildings:
                if i.health > 0:
                    for j in range(i.width):
                        for k in range(i.height):
                            if abs(i.TLx + j - self.x) + abs(i.TLy + k - self.y) < min_distance:
                                min_distance = abs(
                                    i.TLx + j - self.x) + abs(i.TLy + k - self.y)
                                building_to_attack = i
                                final_pos = [i.TLx + j, i.TLy + k]
        if min_distance != np.Inf:
            if min_distance == 0:
                if(self.health > 0):
                    building_to_attack.health = building_to_attack.health - self.damage
            else:
                if self.x < final_pos[0]:
                    self.x = self.x + 1
                elif self.x > final_pos[0]:
                    self.x = self.x - 1
                if self.y < final_pos[1]:
                    self.y = self.y + 1
                elif self.y > final_pos[1]:
                    self.y = self.y - 1
        if self.board.screen[self.y][self.x] == Fore.LIGHTMAGENTA_EX + "!":
            if self.x < final_pos[0]:
                self.x = self.x + 1
            elif self.x > final_pos[0]:
                self.x = self.x - 1
            if self.y < final_pos[1]:
                self.y = self.y + 1
            elif self.y > final_pos[1]:
                self.y = self.y - 1
        self.board.screen[self.y][self.x] = self.shape
        self.bpos.screen[self.y][self.x] = 'L'


class Archer(object):

    def __init__(self, board, bpos, x, y, shape):
        self.health = 50
        self.damage = 10
        self.speed = 2
        self.x = x
        self.y = y
        self.shape = shape
        self.board = board
        self.bpos = bpos

    def rage(self):
        self.damage = self.damage*2
        self.speed = self.speed*2

    def render(self):
        if self.health > 0:
            self.board.screen[self.y][self.x] = self.shape
            self.bpos.screen[self.y][self.x] = 'A'
        else:
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '

    def heal(self):
        self.health = min(self.health * 1.50, 50)

    def check(self):
        if self.health <= 0:
            self.shape = ' '
            self.health = 0
            self.board.screen[self.y][self.x] = ' '
            self.bpos.screen[self.y][self.x] = ' '

    def move(self):
        self.board.screen[self.y][self.x] = ' '
        self.bpos.screen[self.y][self.x] = ' '
        min_distance = np.Inf
        for i in list_of_buildings:
            if i.health > 0:
                for j in range(i.width):
                    for k in range(i.height):
                        if abs(i.TLx + j - self.x) + abs(i.TLy + k - self.y) < min_distance:
                            min_distance = abs(
                                i.TLx + j - self.x) + abs(i.TLy + k - self.y)
                            building_to_attack = i
                            final_pos = [i.TLx + j, i.TLy + k]
        if min_distance != np.Inf:
            if min_distance == 6:
                if(self.health > 0):
                    building_to_attack.health = building_to_attack.health - self.damage
            else:
                if self.x < final_pos[0]:
                    self.x = self.x + 1
                elif self.x > final_pos[0]:
                    self.x = self.x - 1
                if self.y < final_pos[1]:
                    self.y = self.y + 1
                elif self.y > final_pos[1]:
                    self.y = self.y - 1
        self.board.screen[self.y][self.x] = self.shape
        self.bpos.screen[self.y][self.x] = 'A'


os.system('clear')

brd = Screen(height, width, screen)
Bpos = Screen(height, width, build_pres)

# external walls
for y in range(0, height):
    if(y == 0 or y == height-1):
        for x in range(0, width):
            brd.screen[y][x] = "_"
    else:
        brd.screen[y][0] = "|"
        brd.screen[y][width - 1] = "|"

# spawning points

brd.screen[6][0] = Fore.LIGHTRED_EX + "b"
brd.screen[15][width - 1] = Fore.LIGHTRED_EX + "n"
brd.screen[height - 7][0] = Fore.LIGHTRED_EX + "m"

brd.screen[10][0] = Fore.LIGHTYELLOW_EX + "x"
brd.screen[11][width - 1] = Fore.LIGHTYELLOW_EX + "c"
brd.screen[18][width-1] = Fore.LIGHTYELLOW_EX + "v"

brd.screen[0][20] = Fore.LIGHTWHITE_EX + "y"
brd.screen[6][width - 1] = Fore.LIGHTWHITE_EX + "i"
brd.screen[height-1][40] = Fore.LIGHTWHITE_EX + "u"

# brd.draw()

cannon_pos = [(29, 12), (46, 19), (63, 12)]
hut_pos = [(18, 10), (34, 18), (62, 18), (74, 10), (62, 6), (34, 6)]
wiz_pos = [(46, 22), (34, 10)]
th_pos = [(46, 12)]

def level_1 (cannons, wizt, huts): 
    for y in range(0, 9):
        if(y == 0 or y == 8):
            for x in range(0, 15):
                brd.screen[9 + y][40 + x] = Fore.LIGHTMAGENTA_EX + "!"
                Bpos.screen[9 + y][40 + x] = "Wall"
        else:
            brd.screen[9 + y][40 + 0] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 0] = "Wall"
            brd.screen[9 + y][40 + 14] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 14] = "Wall"
    
    # cannons 3
    for i in range(0, len(cannon_pos)):
        c = Cannon(brd, Bpos, "cannon"+str(i+1), 2, 3,
                cannon_pos[i][0], cannon_pos[i][1], Fore.LIGHTGREEN_EX+"c")
        cannons.append(c)
        c.render()

    # wizard tower 2
    for i in range(0, len(wiz_pos)):
        w = WizTower(brd, Bpos, "wizard" + str(i+1), 2, 2,
                    wiz_pos[i][0], wiz_pos[i][1], Fore.LIGHTGREEN_EX + "w")
        wizt.append(w)
        w.render()

    # huts 5
    for i in range(0, len(hut_pos)):
        h = Buildings(brd, Bpos, "hut" + str(i+1), 2, 2,
                    hut_pos[i][0], hut_pos[i][1], Fore.LIGHTGREEN_EX + "h")
        huts.append(h)
        h.render()

# Town hall
th = Buildings(brd, Bpos, "th", 3, 4, th_pos[0][0],
                th_pos[0][1], Fore.LIGHTGREEN_EX + "&")
th.render()
th.health = 200

def level_2 (cannons, wizt, huts):
    level_1(cannons, wizt, huts)
    level.clear()
    level.append(2)
    # cannons 4, wiz 3, huts 5
    trp_cnt.clear()
    trp_cnt.append(0)
    trp_cnt.append(0)
    trp_cnt.append(0)
    for i in bian_list:
        i.health = 0
        i.render()
    for i in arch_list:
        i.health = 0
        i.render()
    for i in loon_list:
        i.health = 0
        i.render()
    bian_list.clear()
    arch_list.clear()
    loon_list.clear()
    # th.health = 200
    # th.render()
    king.health = 0
    king.render()
    king.health = 200
    king.x = 5
    king.y = 28
    king.render()
    cannon_pos.append((46, 6))
    cannons.append(Cannon(brd, Bpos, "cannon4", 2, 3,
                cannon_pos[3][0], cannon_pos[3][1], Fore.LIGHTGREEN_EX+"c"))
    cannons[3].render()
    wiz_pos.append((60, 10))
    wizt.append(WizTower(brd, Bpos, "wizard3", 2, 2,
                    wiz_pos[2][0], wiz_pos[2][1], Fore.LIGHTGREEN_EX + "w"))
    wizt[2].render()
    th = Buildings(brd, Bpos, "th", 3, 4, th_pos[0][0],
                th_pos[0][1], Fore.LIGHTGREEN_EX + "&")
    th.render()
    th.health = 200
    limit.clear()
    limit.append(10)
    limit.append(8)
    limit.append(6)
    for y in range(0, 9):
        if(y == 0 or y == 8):
            for x in range(0, 15):
                brd.screen[9 + y][40 + x] = Fore.LIGHTMAGENTA_EX + "!"
                Bpos.screen[9 + y][40 + x] = "Wall"
        else:
            brd.screen[9 + y][40 + 0] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 0] = "Wall"
            brd.screen[9 + y][40 + 14] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 14] = "Wall"

def level_3(cannons, wizt, huts):
    # cannons 5, wiz 4, huts 5
    level_1(cannons, wizt, huts)
    level.clear()
    level.append(3)
    trp_cnt.clear()
    trp_cnt.append(0)
    trp_cnt.append(0)
    trp_cnt.append(0)
    king.health = 0
    king.render()
    king.health = 200
    king.x = 5
    king.y = 28
    king.render()
    for i in bian_list:
        i.health = 0
        i.render()
    for i in arch_list:
        i.health = 0
        i.render()
    for i in loon_list:
        i.health = 0
        i.render()
    bian_list.clear()
    arch_list.clear()
    loon_list.clear()
    # cannon_pos.append((46, 6))
    cannons.append(Cannon(brd, Bpos, "cannon4", 2, 3,
                cannon_pos[3][0], cannon_pos[3][1], Fore.LIGHTGREEN_EX+"c"))
    cannons[3].render()
    # wiz_pos.append((60, 10))
    wizt.append(WizTower(brd, Bpos, "wizard3", 2, 2,
                    wiz_pos[2][0], wiz_pos[2][1], Fore.LIGHTGREEN_EX + "w"))
    wizt[2].render()    
    cannon_pos.append((29, 18))
    cannons.append(Cannon(brd, Bpos, "cannon5", 2, 3,
                cannon_pos[4][0], cannon_pos[4][1], Fore.LIGHTGREEN_EX+"c"))
    cannons[4].render()
    wiz_pos.append((63, 22))
    wizt.append(WizTower(brd, Bpos, "wizard4", 2, 2,
                    wiz_pos[3][0], wiz_pos[3][1], Fore.LIGHTGREEN_EX + "w"))
    wizt[3].render()
    th = Buildings(brd, Bpos, "th", 3, 4, th_pos[0][0],
                th_pos[0][1], Fore.LIGHTGREEN_EX + "&")
    th.render()
    th.health = 200
    limit.clear()
    limit.append(11)
    limit.append(9)
    limit.append(7)
    for y in range(0, 9):
        if(y == 0 or y == 8):
            for x in range(0, 15):
                brd.screen[9 + y][40 + x] = Fore.LIGHTMAGENTA_EX + "!"
                Bpos.screen[9 + y][40 + x] = "Wall"
        else:
            brd.screen[9 + y][40 + 0] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 0] = "Wall"
            brd.screen[9 + y][40 + 14] = Fore.LIGHTMAGENTA_EX + "!"
            Bpos.screen[9 + y][40 + 14] = "Wall"

play = True

# King

king = King(brd, "King", 5, 28, Fore.LIGHTCYAN_EX + "K")
king.render()


brd.draw()

bian_list = []
arch_list = []
loon_list = []



lastdir = "w"

level_1(cannons, wizt, huts)

# play
while play:
    if len(str_tme) > 0:
        if int(time.time()) == int(str_tme[0]):
            # print("HERE\nHERE\nHERE\n|HERere\n\n\n\n\n\n\n\n")
            str_tme.clear()
            for i in builds_str:
                # print(i.name)
                if(i.shape == Fore.LIGHTGREEN_EX + "&" and i.shape == Fore.LIGHTRED_EX + "&" and i.shape == Fore.LIGHTYELLOW_EX + "&"):
                    th.health -= king.damage*0.75
                    th.girgeet()
                else:
                    i.health -= king.damage*0.75
                    i.girgit()
    # for i in loon_list:
    #     print(i.health)

    alive_bar = '*' * int(int(king.health)/10)
    na_bar = ' ' * (20 - int(king.health/10))
    print(Fore.RESET + Back.RESET + Style.RESET_ALL + "Health Bar" +
          '|' + Fore.GREEN + alive_bar + Fore.RED + na_bar + Fore.RESET + '|')

    print("Number of Barbs alive :", len(bian_list), end = "| ")
    print("Number of Archs alive :", len(arch_list), end = "| ")
    print("Number of Loons alive :", len(loon_list))

    inp = input_to(Get())
    for i in cannons:
        i.attack()
    for i in wizt:
        i.attack()

    if(inp == "w"):
        lastdir = "w"
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y - 1][king.x] == " "):
                brd.screen[king.y][king.x] = " "
                king.y -= 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "s"):
        lastdir = "s"
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y + 1][king.x] == " "):
                brd.screen[king.y][king.x] = " "
                king.y += 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "a"):
        lastdir = "a"
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y][king.x - 1] == " "):
                brd.screen[king.y][king.x] = " "
                king.x -= 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "d"):
        lastdir = "d"
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y][king.x + 1] == " "):
                brd.screen[king.y][king.x] = " "
                king.x += 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "h"):
        king.heal()
        for j in bian_list:
            j.heal()
        for j in arch_list:
            j.heal()
    elif (inp == "r"):
        if(val=="1"):
            king.rage()
        elif(val=="0"):
            king.rage()
            king.damage = king.damage*0.75
        for j in bian_list:
            j.rage()
        for j in arch_list:
            j.rage()
        for j in loon_list:
            j.rage()
    elif(inp == "b"):
        if(trp_cnt[0] < limit[0]):
            bian = Barbarian(brd, Bpos, 1, 6, Fore.MAGENTA + "^")
            bian.render()
            bian_list.append(bian)
            trp_cnt[0] += 1
    elif(inp == "n"):
        if(trp_cnt[0] < limit[0]):
            bian = Barbarian(brd, Bpos, width - 2, 15, Fore.MAGENTA + "^")
            bian.render()
            bian_list.append(bian)
            trp_cnt[0] += 1

    elif(inp == "m"):
        if(trp_cnt[0] < limit[0]):
            bian = Barbarian(brd, Bpos, 1, height - 7, Fore.MAGENTA + "^")
            bian.render()
            bian_list.append(bian)
            trp_cnt[0] += 1

    elif(inp == "x"):
        if(trp_cnt[1] < limit[1]):
            arch = Archer(brd, Bpos, 1, 10, Fore.YELLOW + "$")
            arch.render()
            arch_list.append(arch)
            trp_cnt[1] += 1
    elif(inp == "c"):
        if(trp_cnt[1] < limit[1]):
            arch = Archer(brd, Bpos, width - 2, 11, Fore.YELLOW + "$")
            arch.render()
            arch_list.append(arch)
            trp_cnt[1] += 1

    elif(inp == "v"):
        if(trp_cnt[1] < limit[1]):
            arch = Archer(brd, Bpos, width - 2, 18, Fore.YELLOW + "$")
            arch.render()
            arch_list.append(arch)
            trp_cnt[1] += 1

    elif(inp == "y"):
        if(trp_cnt[2] < limit[2]):
            l = Loons(brd, Bpos, 20, 1, Fore.LIGHTWHITE_EX + "?")
            l.render()
            loon_list.append(l)
            trp_cnt[2] += 1

    elif(inp == "u"):
        if(trp_cnt[2] < limit[2]):
            l = Loons(brd, Bpos, 40, height-2, Fore.LIGHTWHITE_EX + "?")
            l.render()
            loon_list.append(l)
            trp_cnt[2] += 1

    elif(inp == "i"):
        if(trp_cnt[2] < limit[2]):
            l = Loons(brd, Bpos, width - 2, 6, Fore.LIGHTWHITE_EX + "?")
            l.render()
            loon_list.append(l)
            trp_cnt[2] += 1

    elif (inp == "o" and val == "1"):
        for z in range(6):
            #  checking right
            if(king.x + z < 100 and brd.screen[king.y][king.x + z] != " " and brd.screen[king.y][king.x + z] != "-" and brd.screen[king.y][king.x+z] != "|" and brd.screen[king.y][king.x+z] != "b"):
                # attacking cannons
                if (king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y][king.x+z]
                    for i in cannons:
                        if(i.name == num_cannon):
                            i.health -= king.damage
                            i.girgit()
                
                # attacking wiztow
                if (king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "w") or (brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "w") or (brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "w"):
                    num_wiz = Bpos.screen[king.y][king.x+z]
                    for i in wizt:
                        if(i.name == num_wiz):
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y][king.x+z]
                    for i in huts:
                        if(i.name == num_hut):
                            i.health -= king.damage
                            i.girgit()

                elif(king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "&"):
                    th.health -= king.damage
                    th.girgeet()
                elif(king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTMAGENTA_EX + "!"):
                    brd.screen[king.y][king.x+z] = " "
                    Bpos.screen[king.y][king.x+z] = " "

            #  checking left
            if(king.x - z > 0 and brd.screen[king.y][king.x - z] != " " and brd.screen[king.y][king.x-z] != "-" and brd.screen[king.y][king.x-z] != "|" and brd.screen[king.y][king.x-z] != "b"):
                # attacking cannons
                if(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y][king.x-z]
                    for i in cannons:
                        if(i.name == num_cannon):
                            i.health -= king.damage
                            i.girgit()

                # attacking wiztow
                if(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y][king.x-z]
                    num_wiz = Bpos.screen[king.y][king.x-z]
                    for i in wizt:
                        if(i.name == num_wiz):
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y][king.x-z]
                    for i in huts:
                        if(i.name == num_hut):
                            i.health -= king.damage
                            i.girgit()

                elif(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "&"):
                    th.health -= king.damage
                    th.girgeet()
                elif(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTMAGENTA_EX + "!"):
                    brd.screen[king.y][king.x-z] = " "
                    Bpos.screen[king.y][king.x-z] = " "

        #  checking up
            if(king.y + z < 30 and brd.screen[king.y + z][king.x] != " " and brd.screen[king.y + z][king.x] != "-" and brd.screen[king.y + z][king.x] != "|" and brd.screen[king.y + z][king.x] != "b"):

                # attacking cannons
                if(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y + z][king.x]
                    for i in cannons:
                        if(i.name == num_cannon):
                            i.health -= king.damage
                            i.girgit()
                
                # attacking wiztow
                if(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                    num_wiz = Bpos.screen[king.y + z][king.x]
                    for i in wizt:
                        if(i.name == num_wiz):
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y + z][king.x]
                    for i in huts:
                        if(i.name == num_hut):
                            i.health -= king.damage
                            i.girgit()

                elif(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                    th.health -= king.damage
                    th.girgeet()
                elif(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                    brd.screen[king.y + z][king.x] = " "
                    Bpos.screen[king.y + z][king.x] = " "

        #  checking down
            if(king.y - z > 0 and brd.screen[king.y - z][king.x] != " " and brd.screen[king.y - z][king.x] != "-" and brd.screen[king.y - z][king.x] != "|" and brd.screen[king.y - z][king.x] != "b"):
                # attacking cannons
                if(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y - z][king.x]
                    for i in cannons:
                        if(i.name == num_cannon):
                            i.health -= king.damage
                            i.girgit()
                
                # attacking wiztow
                if(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                    num_wiz = Bpos.screen[king.y - z][king.x]
                    for i in wizt:
                        if(i.name == num_wiz):
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y - z][king.x]
                    for i in huts:
                        if(i.name == num_hut):
                            i.health -= king.damage
                            i.girgit()

                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                    th.health -= king.damage
                    th.girgeet()
                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                    brd.screen[king.y - z][king.x] = " "
                    Bpos.screen[king.y - z][king.x] = " "

    elif (inp == "o"):
        locats = []
        posn = []
        if lastdir == "w":
            posn = [-16, 0]
        elif lastdir == "a":
            posn = [0, -16]
        elif lastdir == "s":
            posn = [16, 0]
        elif lastdir == "d":
            posn = [0, 16]
        
        for i in range(-4,5):
            for j in range(-4,5):
                locats.append([posn[0]+i, posn[1]+j])
        str_tme.clear()
        # print(time.time())
        str_tme.append(time.time() + 1)
        store_build = []
        for z in locats:
            if king.y + z[0] >= 0 and king.y + z[0] <= brd.height - 1 and king.x + z[1] >= 0 and king.x + z[1] <= brd.width - 1:
            # king.y + z[0], king.x + z[1]
                if(brd.screen[king.y + z[0]][king.x+z[1]] != " " and brd.screen[king.y + z[0]][king.x+z[1]] != "-" and brd.screen[king.y + z[0]][king.x+z[1]] != "|" and brd.screen[king.y + z[0]][king.x+z[1]] != "b"):
                    # attacking cannons
                    if (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "c"):
                        num_cannon = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in cannons:
                            if(i.name == num_cannon):
                                store_build.append(i)

                    # attacking wiztow
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "w" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "w" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "w"):
                        num_wiz = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in wizt:
                            if(i.name == num_wiz):
                                store_build.append(i)

                    # attacking huts
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "h"):
                        num_hut = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in huts:
                            if(i.name == num_hut):
                                store_build.append(i)
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "&"):
                        store_build.append(th)
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTMAGENTA_EX + "!"):
                        brd.screen[king.y + z[0]][king.x+z[1]] = " "
                        Bpos.screen[king.y + z[0]][king.x+z[1]] = " "

        # res = []
        builds_str.clear()
        [builds_str.append(x) for x in store_build if x not in builds_str]
        # print(builds_str)

    elif(inp == " " and val == "1"):
        #  checking right
        if(brd.screen[king.y][king.x + 1] != " " and brd.screen[king.y][king.x+1] != "-" and brd.screen[king.y][king.x+1] != "|" and brd.screen[king.y][king.x+1] != "b"):
            # attacking cannons
            if (brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y][king.x+1]
                for i in cannons:
                    if(i.name == num_cannon):
                        i.health -= king.damage
                        i.girgit()

            # attacking wiztow
            elif((brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "w") or (brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "w") or (brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "w")):
                num_wiz = Bpos.screen[king.y][king.x+1]
                for i in wizt:
                    if(i.name == num_wiz):
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y][king.x+1]
                for i in huts:
                    if(i.name == num_hut):
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "&"):
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y][king.x+1] = " "
                Bpos.screen[king.y][king.x+1] = " "

        #  checking left
        if(brd.screen[king.y][king.x - 1] != " " and brd.screen[king.y][king.x-1] != "-" and brd.screen[king.y][king.x-1] != "|" and brd.screen[king.y][king.x-1] != "b"):

            # attacking cannons
            if(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y][king.x-1]
                for i in cannons:
                    if(i.name == num_cannon):
                        i.health -= king.damage
                        i.girgit()

            # attacking wiztow
            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "w" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "w" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "w"):
                num_wiz = Bpos.screen[king.y][king.x-1]
                for i in wizt:
                    if(i.name == num_wiz):
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y][king.x-1]
                for i in huts:
                    if(i.name == num_hut):
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "&"):
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y][king.x-1] = " "
                Bpos.screen[king.y][king.x-1] = " "

    #  checking up
        if(brd.screen[king.y + 1][king.x] != " " and brd.screen[king.y + 1][king.x] != "-" and brd.screen[king.y + 1][king.x] != "|" and brd.screen[king.y + 1][king.x] != "b"):

            # attacking cannons
            if(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y + 1][king.x]
                for i in cannons:
                    if(i.name == num_cannon):
                        i.health -= king.damage
                        i.girgit()

            # attacking wiztow
            elif(brd.screen[king.y+1][king.x] == Fore.LIGHTGREEN_EX + "w" or brd.screen[king.y+1][king.x] == Fore.LIGHTRED_EX + "w" or brd.screen[king.y+1][king.x] == Fore.LIGHTYELLOW_EX + "w"):
                num_wiz = Bpos.screen[king.y+1][king.x]
                for i in wizt:
                    if(i.name == num_wiz):
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y + 1][king.x]
                for i in huts:
                    if(i.name == num_hut):
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y + 1][king.x] = " "
                Bpos.screen[king.y + 1][king.x] = " "

    #  checking down
        if(brd.screen[king.y - 1][king.x] != " " and brd.screen[king.y - 1][king.x] != "-" and brd.screen[king.y - 1][king.x] != "|" and brd.screen[king.y - 1][king.x] != "b"):
            # attacking cannons
            if(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y - 1][king.x]
                for i in cannons:
                    if(i.name == num_cannon):
                        i.health -= king.damage
                        i.girgit()

            # attacking wiztow
            elif(brd.screen[king.y-1][king.x] == Fore.LIGHTGREEN_EX + "w" or brd.screen[king.y-1][king.x] == Fore.LIGHTRED_EX + "w" or brd.screen[king.y-1][king.x] == Fore.LIGHTYELLOW_EX + "w"):
                num_wiz = Bpos.screen[king.y-1][king.x]
                for i in wizt:
                    if(i.name == num_wiz):
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y - 1][king.x]

                for i in huts:
                    if(i.name == num_hut):
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y - 1][king.x] = " "
                Bpos.screen[king.y - 1][king.x] = " "

    elif(inp == " "):
        locats = []
        posn = []
        if lastdir == "w":
            posn = [-8, 0]
        elif lastdir == "a":
            posn = [0, -8]
        elif lastdir == "s":
            posn = [8, 0]
        elif lastdir == "d":
            posn = [0, 8]
        
        for i in range(-2,3):
            for j in range(-2,3):
                locats.append([posn[0]+i, posn[1]+j])
        
        store_build = []
        for z in locats:
            if king.y + z[0] >= 0 and king.y + z[0] <= brd.height - 1 and king.x + z[1] >= 0 and king.x + z[1] <= brd.width - 1:
            # king.y + z[0], king.x + z[1]
                if(brd.screen[king.y + z[0]][king.x+z[1]] != " " and brd.screen[king.y + z[0]][king.x+z[1]] != "-" and brd.screen[king.y + z[0]][king.x+z[1]] != "|" and brd.screen[king.y + z[0]][king.x+z[1]] != "b"):
                    # attacking cannons
                    if (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "c"):
                        num_cannon = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in cannons:
                            if(i.name == num_cannon):
                                store_build.append(i)

                    # attacking wiztow
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "w" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "w" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "w"):
                        num_wiz = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in wizt:
                            if(i.name == num_wiz):
                                store_build.append(i)

                    # attacking huts
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "h"):
                        num_hut = Bpos.screen[king.y + z[0]][king.x+z[1]]
                        for i in huts:
                            if(i.name == num_hut):
                                store_build.append(i)
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTYELLOW_EX + "&"):
                        store_build.append(th)
                    elif(brd.screen[king.y + z[0]][king.x+z[1]] == Fore.LIGHTMAGENTA_EX + "!"):
                        brd.screen[king.y + z[0]][king.x+z[1]] = " "
                        Bpos.screen[king.y + z[0]][king.x+z[1]] = " "

        res = []
        [res.append(x) for x in store_build if x not in res]

        for i in res:
            if(i.shape == Fore.LIGHTGREEN_EX + "&" and i.shape == Fore.LIGHTRED_EX + "&" and i.shape == Fore.LIGHTYELLOW_EX + "&"):
                th.health -= king.damage*0.75
                th.girgeet()
            else:
                i.health -= king.damage*0.75
                i.girgit()

    elif(inp == "q"):
        # file.close()
        play = False

    if inp == None:
        file.write('-')
    else:
        file.write(inp)
    file.write('\n')
    os.system("clear")

    for i in list_of_buildings:
        if(i.status):
            i.render()
            if(i.name[0] == 't'):
                i.girgeet()
            else:
                i.girgit()

    for i in bian_list:
        if i.health <= 0:
            brd.screen[i.y][i.x] = " "
            bian_list.remove(i)
            continue
        i.check()
        locomo = i.speed
        while(locomo > 0):
            i.move()
            locomo -= 1

    for i in arch_list:
        if i.health <= 0:
            brd.screen[i.y][i.x] = " "
            arch_list.remove(i)
            continue
        locomo = i.speed
        while(locomo > 0):
            i.move()
            locomo -= 1

    for i in loon_list:
        if i.health <= 0:
            brd.screen[i.y][i.x] = " "
            loon_list.remove(i)
            continue
        locomo = i.speed
        while(locomo > 0):
            i.move()
            locomo -= 1

    king.render()
    brd.draw()

    if(Total == 0 and level[0] == 1):
        os.system("clear")
        os.system('aplay -q sounds_win.wav&')
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " __     __                             _ ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " \ \   / /                            | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "  \ \_/ /_ _  __ _  __ _  __ _ _   _  | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "   \   / _` |/ _` |/ _` |/ _` | | | | | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    | | (_| | (_| | (_| | (_| | |_| | |_|".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    |_|\__,_|\__,_|\__,_|\__,_|\__, | (_)".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                __/ |    ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                               |___/     ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                         ".center(width)+Style.RESET_ALL)
        # file.close()
        level_2(cannons,wizt,huts)
        # play = False
    elif(Total == 0 and level[0] == 2):
        os.system("clear")
        os.system('aplay -q sounds_win.wav&')
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " __     __                             _ ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " \ \   / /                            | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "  \ \_/ /_ _  __ _  __ _  __ _ _   _  | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "   \   / _` |/ _` |/ _` |/ _` | | | | | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    | | (_| | (_| | (_| | (_| | |_| | |_|".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    |_|\__,_|\__,_|\__,_|\__,_|\__, | (_)".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                __/ |    ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                               |___/     ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                         ".center(width)+Style.RESET_ALL)
        # file.close()
        level_3(cannons,wizt,huts)
        # play = False
    elif(Total == 0 and level[0] == 3):
        os.system("clear")
        os.system('aplay -q sounds_win.wav&')
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " __     __                             _ ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " \ \   / /                            | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "  \ \_/ /_ _  __ _  __ _  __ _ _   _  | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "   \   / _` |/ _` |/ _` |/ _` | | | | | |".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    | | (_| | (_| | (_| | (_| | |_| | |_|".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "    |_|\__,_|\__,_|\__,_|\__,_|\__, | (_)".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                __/ |    ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                               |___/     ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                         ".center(width)+Style.RESET_ALL)
        # file.close()
        # level_2(cannons,wizt,huts)
        play = False
    if(not bian_list and king.health <= 0 and not arch_list and not loon_list):
        os.system("clear")
        os.system('aplay -q game_over.wav&')
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                                     ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "  _____                         ____                 ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " / ____|                       / __ \                ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "| |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "| | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "| |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              " \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ".center(width))
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                                     ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                                     ".center(width)+Style.RESET_ALL)
        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +
              "                                                     ".center(width)+Style.RESET_ALL)
        # file.close()
        play = False
file.close()
