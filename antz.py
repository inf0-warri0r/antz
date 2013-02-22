#!/usr/bin/env python

"""
Author : tharindra galahena (inf0_warri0r)
Project: ant colony simulation
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 22/02/2013
License:

     Copyright 2012 Tharindra Galahena

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version. This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.

* You should have received a copy of the GNU General Public License along with
This program. If not, see http://www.gnu.org/licenses/.

"""

import random


class world:

    def __init__(self):
        self.width = 100
        self.height = 100
        self.grid = list()
        self.hive = 50, 50
        self.ants = list()
        self.paths = list()

        self.num_of_ants = 40
        self.food_count = 1

        for i in range(0, self.height):
            self.grid.append(list())

        for i in range(0, self.height):
            for j in range(0, self.width):
                self.grid[i].append(0)

        for i in range(0, self.height):
            self.ants.append(ant(self.hive))

        l = random.randrange(0, 100)
        m = random.randrange(0, 100)
        while self.grid[l][m] == '1' or self.grid[m][l] == '1':
            l = random.randrange(0, 100)
            m = random.randrange(0, 100)

        self.food = (l, m)
        self.food_amount = 100

    def move(self):
        for i in range(0, self.num_of_ants):
            if len(self.ants[i].path) <= 0:
                if self.ants[i].x == self.food[0]:
                    if self.ants[i].y == self.food[1]:
                        if self.ants[i].mode != 'f':
                            path = self.ants[i].used_path[:]
                            self.ants[i].used_path = list()
                            path.reverse()
                            for j in range(0, len(path)):
                                if path[j][0] == self.hive:
                                    print "b"
                                    break
                                self.grid[path[j][0][0]][path[j][0][1]] = 3
                            self.grid[self.ants[i].x][self.ants[i].y] = 0
                            self.grid[self.hive[0]][self.hive[1]] = 0
                        else:
                            if self.ants[i].target == self.food:
                                #print "food"
                                if len(self.ants[i].pr_path) > 0:
                                    for mx_p in self.ants[i].pr_path:
                                        a = self.grid[mx_p[0]][mx_p[1]]
                                        #if a < 20:
                                        self.grid[mx_p[0]][mx_p[1]] = a + 3
                                    self.ants[i].pr_path = list()
                                    self.grid[self.hive[0]][self.hive[1]] = 0
                                    self.grid[self.ants[i].x][self.ants[i].y] = 0
                            else:
                                #print "wrong food"
                                if len(self.ants[i].pr_path) > 0:
                                    #print "-----"
                                    for mx_p in self.ants[i].pr_path:
                                        a = self.grid[mx_p[0]][mx_p[1]]
                                        #if a > 0:
                                        self.grid[mx_p[0]][mx_p[1]] = a - 3
                                    self.ants[i].pr_path = list()
                                    self.grid[self.hive[0]][self.hive[1]] = 0
                                    self.grid[self.ants[i].x][self.ants[i].y] = 0
                        self.ants[i].mode = 'f'
                        self.ants[i].target = self.hive
                        self.food_amount = self.food_amount - 1

                if self.ants[i].x == self.hive[0]:
                    if self.ants[i].y == self.hive[1]:
                        if self.ants[i].mode == 'f':
                            if self.ants[i].target == self.hive:
                                #print "hive"
                                self.ants[i].target = self.food
                                if len(self.ants[i].pr_path) > 0:
                                    for mx_p in self.ants[i].pr_path:
                                        a = self.grid[mx_p[0]][mx_p[1]]
                                        if a < 20:
                                            self.grid[mx_p[0]][mx_p[1]] = a
                                    self.ants[i].pr_path = list()
                                    self.grid[self.food[0]][self.food[1]] = 0
                            else:
                                #print "wrong hive"
                                if len(self.ants[i].pr_path) > 0:
                                    #print "-----"
                                    for mx_p in self.ants[i].pr_path:
                                        a = self.grid[mx_p[0]][mx_p[1]]
                                        if a > 0:
                                            self.grid[mx_p[0]][mx_p[1]] = a - 3
                                    self.ants[i].pr_path = list()
                                    self.grid[self.hive[0]][self.hive[1]] = 0
                                    self.grid[self.ants[i].x][self.ants[i].y] = 0

                if self.ants[i].mode != 'f':
                    if self.grid[self.ants[i].x][self.ants[i].y] > 0:
                        self.ants[i].mode = 'f'
                        self.ants[i].target = self.hive

                if self.ants[i].mode == 'f':
                    x = self.ants[i].x
                    y = self.ants[i].y
                    mx = -1.0
                    mx_p = (x, y)
                    for k in range(-1, 2):
                        for j in range(-1, 2):
                            if k == 0 and j == 0:
                                continue
                            if self.ants[i].x + j >= self.width:
                                continue
                            if self.ants[i].x + j < 0:
                                continue
                            if self.ants[i].y + k >= self.height:
                                continue
                            if self.ants[i].y + k < 0:
                                continue
                            if self.ants[i].x_2 == self.ants[i].x + j:
                                if self.ants[i].y_2 == self.ants[i].y + k:
                                    continue
                            ne = 100.0 / (1.0 + self.ants[i].h(x + j, y + k,
                                    self.ants[i].target[0],
                                    self.ants[i].target[1]))
                            pr = self.grid[x + j][y + k] / 5.0
                            print "sm = ", ne, " ", pr
                            sm = ne + pr
                            if sm > mx:
                                mx = sm
                                mx_p = (x + j, y + k)

                    self.ants[i].x_2 = self.ants[i].x
                    self.ants[i].y_2 = self.ants[i].y
                    self.ants[i].x = mx_p[0]
                    self.ants[i].y = mx_p[1]

                    a = self.grid[mx_p[0]][mx_p[1]]
                    if a > 0:
                        self.grid[mx_p[0]][mx_p[1]] = a - 1
                    self.ants[i].pr_path.append(mx_p)

                else:
                    path = self.ants[i].check_trail(self.grid, self.width,
                                        self.height)
                    self.ants[i].path = self.ants[i].find_food(self.grid,
                                        self.width, self.height, self.food)
            else:
                ((x, y), p) = self.ants[i].path[0]
                self.ants[i].x_2 = self.ants[i].x
                self.ants[i].y_2 = self.ants[i].y
                self.ants[i].x = x
                self.ants[i].y = y
                self.ants[i].used_path.append(((x, y), p))
                self.ants[i].path.remove(((x, y), p))

        if self.food_amount <= 0:
            for i in range(0, self.num_of_ants):
                self.ants[i].mode = 'r'
            for i in range(0, self.height):
                for j in range(0, self.width):
                    self.grid[j][i] = 0

            x = random.randrange(0, 100)
            y = random.randrange(0, 100)
            while self.grid[x][y] == '1' or self.grid[y][x] == '1':
                x = random.randrange(0, 100)
                y = random.randrange(0, 100)
            self.food = (x, y)
            self.food_amount = 100


class ant:

    def __init__(self, start):
        self.x = start[0]
        self.y = start[1]
        self.x_2 = 0
        self.y_2 = 0
        self.inc_x = random.randrange(-1, 2)
        self.inc_y = random.randrange(-1, 2)
        self.with_food = False
        self.search_space = 10
        self.path = list()
        self.pr_path = list()
        self.used_path = list()
        self.target = (0, 0)
        self.mode = 'r'
        self.count = 0

    def h(self, sx, sy, dx, dy):
        return ((dx - sx) ** 2.0) ** 0.5 + ((dy - sy) ** 2.0) ** 0.5

    def find_path(self, sx, sy, dx, dy, grid, w, h):
        fring = list()
        x = sx
        y = sy
        visited = {}

        while x != dx or y != dy:

            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    if j < 0 or i < 0 or i >= w or j >= h:
                        continue
                    if j == y and i == x:
                        continue
                    if visited.get((i, j), 'a') == 'a':
                        fring.append((self.h(i, j, dx, dy), i, j, (x, y)))
                        visited[(i, j)] = x, y
            fring = sorted(fring)
            if len(fring) <= 0:
                break
            hu, x, y, l = fring[0]
            fring.remove((hu, x, y, l))

        path = list()
        if x != dx and y != dy:
            return list()
        while x != sx or y != sy:
            path.append(((x, y), 0))
            x, y = visited[(x, y)]

        path.append(((x, y), 1))
        return path

    def find_food(self, grid, w, h, food):
        for j in range(self.y - self.search_space, self.y + self.search_space):
            for i in range(self.x - self.search_space, self.x + self.search_space):
                if i < 0 or j < 0 or i >= w or j >= w:
                    continue
                if food == (i, j):
                    path = self.find_path(self.x, self.y, i, j, grid, w, h)
                    if len(path) != 0:
                        path.reverse()
                        self.with_food = True
                        return path

        if self.count > 5:
            x = random.randrange(-1, 2)
            y = random.randrange(-1, 2)
            self.count = 0
        else:
            x = self.inc_x
            y = self.inc_y
        f1 = self.x + x >= w or self.y + y >= h
        f2 = self.x + x < 0 or self.y + y < 0
        f3 = x == 0 and y == 0
        f4 = self.x + x == self.x_2 and self.y + y == self.y_2
        while f1 or f2 or f3 or f4:
            x = random.randrange(-10, 21) / 10
            y = random.randrange(-10, 21) / 10
            f1 = self.x + x >= w or self.y + y >= h
            f2 = self.x + x < 0 or self.y + y < 0
            f3 = x == 0 and y == 0
            f4 = self.x + x == self.x_2 and self.y + y == self.y_2
        self.inc_x = x
        self.inc_y = y

        self.count = self.count + 1

        self.with_food = False
        return [((self.x + self.inc_x, self.y + self.inc_y), 1)]

    def find_home(self, dx, dy, grid, w, h):
        path = self.find_path(self.x, self.y, dx, dy, grid, w, h)
        if len(path) != 0:
            path.reverse()
        return path

    def check_trail(self, grid, w, h):
        min_x = self.x - self.search_space
        max_x = self.x + self.search_space
        min_y = self.y - self.search_space
        max_y = self.y + self.search_space
        if min_x < 0:
            min_x = 0
        if min_y < 0:
            min_y = 0
        if max_x > w:
            max_x = w - 1
        if max_y > h:
            max_y = h - 1
        for i in range(min_y, max_y):
            for j in range(min_x, max_x):
                if grid[j][i] > 0:
                    path = self.find_path(self.x, self.y, j, i, grid, w, h)
                    if len(path) != 0:
                        path.reverse()
                        return path
        return list()
