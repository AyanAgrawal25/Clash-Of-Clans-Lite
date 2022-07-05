from functools import total_ordering
import random
from colorama import init, Fore, Back, Style
from matplotlib import lines
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
from time import sleep, time
from math import pi
from input import input_to, Get

height = 30
width = 100
Total = 0
screen = [[' ' for x in range(0, width)]
          for y in range(0, height)]

build_pres = [[' ' for x in range(0, width)]
              for y in range(0, height)]


class Screen(object):
    """Class to handle screen."""

    def __init__(self, height, width, screen):
        self.height = height
        self.width = width
        self.screen = screen

    def draw(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                print(Fore.BLUE + self.screen[y][x], end='')
            print()


list_of_buildings = []

class Buildings(object):
    def __init__(self, board, bpos, name, height, width, TLx, TLy, shape):
        self.board = board
        self.status = True
        self.bpos = bpos
        self.range = 6
        self.damage = 30
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

class King(object):

    def __init__(self, board, name, x, y, shape):
        self.name = "King"
        self.health = 200
        self.damage = 20
        self.speed = 1
        self.x = x
        self.y = y
        self.shape = shape
        self.board = board

    def rage(self):
        self.speed = self.speed * 2
        self.damage = self.damage * 2

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
        self.health = min(self.health*1.50, 100)

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
                elif self.y < final_pos[1]:
                    self.y = self.y + 1
                elif self.y > final_pos[1]:
                    self.y = self.y - 1
        self.board.screen[self.y][self.x] = self.shape
        self.bpos.screen[self.y][self.x] = 'B'


os.system('clear')

brd = Screen(height, width, screen)
Bpos = Screen(height, width, build_pres)

# external walls
for y in range(0, height):
    if(y == 0 or y == height-1):
        for x in range(0, width):
            brd.screen[y][x] = "-"
    else:
        brd.screen[y][0] = "|"
        brd.screen[y][width - 1] = "|"

# spawning points

brd.screen[6][0] = Fore.LIGHTRED_EX + "b"
brd.screen[15][width - 1] = Fore.LIGHTRED_EX + "n"
brd.screen[height - 7][0] = Fore.LIGHTRED_EX + "m"

# brd.draw()

cannon_pos = [(25, 12), (46, 21), (65, 12), (46, 5)]
hut_pos = [(6, 20), (22, 21), (70, 21), (85, 10), (65, 5), (46, 12)]
th_pos = [(46, 12)]

# cannons
cannon1 = Buildings(brd, Bpos, "cannon1", 2, 3,
                    cannon_pos[0][0], cannon_pos[0][1], Fore.LIGHTGREEN_EX + "c")
cannon1.render()

cannon2 = Buildings(brd, Bpos, "cannon2", 2, 3,
                    cannon_pos[1][0], cannon_pos[1][1], Fore.LIGHTGREEN_EX + "c")
cannon2.render()

cannon3 = Buildings(brd, Bpos, "cannon3", 2, 3,
                    cannon_pos[2][0], cannon_pos[2][1], Fore.LIGHTGREEN_EX + "c")
cannon3.render()

cannon4 = Buildings(brd, Bpos, "cannon4", 2, 3,
                    cannon_pos[3][0], cannon_pos[3][1], Fore.LIGHTGREEN_EX + "c")
cannon4.render()
# list_of_buildings.append(self)

# huts
hut1 = Buildings(brd, Bpos, "hut1", 2, 2,
                 hut_pos[0][0], hut_pos[0][1], Fore.LIGHTGREEN_EX + "h")
hut1.render()

hut2 = Buildings(brd, Bpos, "hut2", 2, 2,
                 hut_pos[1][0], hut_pos[1][1], Fore.LIGHTGREEN_EX + "h")
hut2.render()

hut3 = Buildings(brd, Bpos, "hut3", 2, 2,
                 hut_pos[2][0], hut_pos[2][1], Fore.LIGHTGREEN_EX + "h")
hut3.render()

hut4 = Buildings(brd, Bpos, "hut4", 2, 2,
                 hut_pos[3][0], hut_pos[3][1], Fore.LIGHTGREEN_EX + "h")
hut4.render()

hut5 = Buildings(brd, Bpos, "hut5", 2, 2,
                 hut_pos[4][0], hut_pos[4][1], Fore.LIGHTGREEN_EX + "h")
hut5.render()

# Town hall
th = Buildings(brd, Bpos, "th", 3, 4, th_pos[0][0],
               th_pos[0][1], Fore.LIGHTGREEN_EX + "&")
th.render()
th.health = 200

# walls
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

file = open(f"replays/{sys.argv[1]}", "r")
lines = file.readlines()
# play
for line in lines:
    
    alive_bar = '*' * int(int(king.health)/10)
    na_bar = ' ' * (20 - int(king.health/10))
    print(Fore.RESET + Back.RESET + Style.RESET_ALL + "Health Bar" +
          '|' + Fore.GREEN + alive_bar + Fore.RED + na_bar + Fore.RESET + '|')
    
    print("Number of Barbs alive :", len(bian_list))

    xxx = input_to(Get())
    inp = line[0]

    if(xxx == "q"):
        break

    for i in list_of_buildings:
        if(i.name[0] == 'c'):
            flag = False
            # for King
            dist1 = abs(king.x - i.TLx) + abs(king.y - i.TLy)
            if(dist1 <= i.range and i.health > 0 and king.health > 0 and flag == False):
                os.system('aplay -q cannon.wav&')
                king.health = king.health - i.damage
                flag = True
            for j in bian_list:
                dist = abs(i.TLx - j.x) + abs(i.TLy - j.y)
                if(dist <= i.range and i.health > 0 and j.health > 0 and flag == False):
                    os.system('aplay -q cannon.wav&')
                    j.health = j.health - i.damage
                    flag = True

    if(inp == "w"):
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y - 1][king.x] == " "):
                brd.screen[king.y][king.x] = " "
                king.y -= 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "s"):
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y + 1][king.x] == " "):
                brd.screen[king.y][king.x] = " "
                king.y += 1
                king.render()
            locomotion = locomotion - 1
    elif(inp == "a"):
        locomotion = king.speed
        while(locomotion > 0):
            if(brd.screen[king.y][king.x - 1] == " "):
                brd.screen[king.y][king.x] = " "
                king.x -= 1
                king.render()
            locomotion = locomotion - 1         
    elif(inp == "d"):
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
    elif(inp == "b"):
        bian = Barbarian(brd, Bpos, 1, 6, Fore.MAGENTA + "^")
        bian.render()
        bian_list.append(bian)
    elif (inp == "r"):
        king.rage()
        for j in bian_list:
            j.rage()
    elif(inp == "n"):
        bian = Barbarian(brd, Bpos, width - 2, 15, Fore.MAGENTA + "^")
        bian.render()
        bian_list.append(bian)
    elif(inp == "m"):
        bian = Barbarian(brd, Bpos, 1, height - 7, Fore.MAGENTA + "^")
        bian.render()
        bian_list.append(bian)
    elif (inp == "o"):
        for z in range(6):
            #  checking right
            if(king.x + z < 100 and brd.screen[king.y][king.x + z] != " " and brd.screen[king.y][king.x + z] != "-" and brd.screen[king.y][king.x+z] != "|" and brd.screen[king.y][king.x+z] != "b"):
                # attacking cannons
                if (king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "c"):
                    num_cannon = Bpos.screen[king.y][king.x+z]
                    for i in list_of_buildings:
                        if(i.name == num_cannon):
                            # i.shape = "c"
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y][king.x+z]

                    for i in list_of_buildings:
                        if(i.name == num_hut):
                            # i.shape = "h"
                            i.health -= king.damage
                            i.girgit()

                elif(king.x + z < 100 and brd.screen[king.y][king.x+z] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x+z] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x+z] == Fore.LIGHTYELLOW_EX + "&"):
                    # th.shape = "&"
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
                    for i in list_of_buildings:
                        if(i.name == num_cannon):
                            # i.shape = "c"
                            i.health -= king.damage
                            i.girgit()

                # attacking huts
                elif(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y][king.x-z]

                    for i in list_of_buildings:
                        if(i.name == num_hut):
                            # i.shape = "h"
                            i.health -= king.damage
                            i.girgit()

                elif(king.x - z > 0 and brd.screen[king.y][king.x-z] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x-z] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x-z] == Fore.LIGHTYELLOW_EX + "&"):
                    # th.shape = "&"
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
                    for i in list_of_buildings:
                        if(i.name == num_cannon):
                            # i.shape = "c"
                            i.health -= king.damage
                            i.girgit()
        
                # attacking huts
                elif(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y + z][king.x]

                    for i in list_of_buildings:
                        if(i.name == num_hut):
                            # i.shape = "h"
                            i.health -= king.damage
                            i.girgit()

                elif(king.y + z < 30 and brd.screen[king.y + z][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + z][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + z][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                    # th.shape = "&"
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
                    for i in list_of_buildings:
                        if(i.name == num_cannon):
                            # i.shape = "c"
                            i.health -= king.damage
                            i.girgit()
        
                # attacking huts
                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                    num_hut = Bpos.screen[king.y - z][king.x]

                    for i in list_of_buildings:
                        if(i.name == num_hut):
                            # i.shape = "h"
                            i.health -= king.damage
                            i.girgit()

                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y - z][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y - z][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                    # th.shape = "&"
                    th.health -= king.damage
                    th.girgeet()
                elif(king.y - z > 0 and brd.screen[king.y - z][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                    brd.screen[king.y - z][king.x] = " "
                    Bpos.screen[king.y - z][king.x] = " "
    elif(inp == " "):
        #  checking right
        if(brd.screen[king.y][king.x + 1] != " " and brd.screen[king.y][king.x+1] != "-" and brd.screen[king.y][king.x+1] != "|" and brd.screen[king.y][king.x+1] != "b"):
            # attacking cannons
            if (brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "c") or (brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "c") or (brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y][king.x+1]
                for i in list_of_buildings:
                    if(i.name == num_cannon):
                        # i.shape = "c"
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y][king.x+1]

                for i in list_of_buildings:
                    if(i.name == num_hut):
                        # i.shape = "h"
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x+1] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x+1] == Fore.LIGHTYELLOW_EX + "&"):
                # th.shape = "&"
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y][king.x+1] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y][king.x+1] = " "
                Bpos.screen[king.y][king.x+1] = " "
                # continue

        #  checking left
        if(brd.screen[king.y][king.x - 1] != " " and brd.screen[king.y][king.x-1] != "-" and brd.screen[king.y][king.x-1] != "|" and brd.screen[king.y][king.x-1] != "b"):

            # attacking cannons
            if(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y][king.x-1]
                for i in list_of_buildings:
                    if(i.name == num_cannon):
                        # i.shape = "c"
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y][king.x-1]

                for i in list_of_buildings:
                    if(i.name == num_hut):
                        # i.shape = "h"
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y][king.x-1] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y][king.x-1] == Fore.LIGHTYELLOW_EX + "&"):
                # th.shape = "&"
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y][king.x-1] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y][king.x-1] = " "
                Bpos.screen[king.y][king.x-1] = " "
                # continue

    #  checking up
        if(brd.screen[king.y + 1][king.x] != " " and brd.screen[king.y + 1][king.x] != "-" and brd.screen[king.y + 1][king.x] != "|" and brd.screen[king.y + 1][king.x] != "b"):

            # attacking cannons
            if(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y + 1][king.x]
                for i in list_of_buildings:
                    if(i.name == num_cannon):
                        # i.shape = "c"
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y + 1][king.x]

                for i in list_of_buildings:
                    if(i.name == num_hut):
                        # i.shape = "h"
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y + 1][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y + 1][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                # th.shape = "&"
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y + 1][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y + 1][king.x] = " "
                Bpos.screen[king.y + 1][king.x] = " "
                # continue

    #  checking down
        if(brd.screen[king.y - 1][king.x] != " " and brd.screen[king.y - 1][king.x] != "-" and brd.screen[king.y - 1][king.x] != "|" and brd.screen[king.y - 1][king.x] != "b"):
            # attacking cannons
            if(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "c" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "c" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "c"):
                num_cannon = Bpos.screen[king.y - 1][king.x]
                for i in list_of_buildings:
                    if(i.name == num_cannon):
                        # i.shape = "c"
                        i.health -= king.damage
                        i.girgit()

            # attacking huts
            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "h" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "h" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "h"):
                num_hut = Bpos.screen[king.y - 1][king.x]

                for i in list_of_buildings:
                    if(i.name == num_hut):
                        # i.shape = "h"
                        i.health -= king.damage
                        i.girgit()

            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTGREEN_EX + "&" or brd.screen[king.y - 1][king.x] == Fore.LIGHTRED_EX + "&" or brd.screen[king.y - 1][king.x] == Fore.LIGHTYELLOW_EX + "&"):
                # th.shape = "&"
                th.health -= king.damage
                th.girgeet()
            elif(brd.screen[king.y - 1][king.x] == Fore.LIGHTMAGENTA_EX + "!"):
                brd.screen[king.y - 1][king.x] = " "
                Bpos.screen[king.y - 1][king.x] = " "
                # continue

    elif(inp == "q"):
        # file.close()
        play = False

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
    
    king.render()

    brd.draw()

    if(Total == 0):
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
        play = False

    if(not bian_list and king.health <= 0):
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
