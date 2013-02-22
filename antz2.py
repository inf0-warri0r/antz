import random
from Tkinter import *
import time


class world:

    def __init__(self):
        self.width = 100
        self.height = 100
        self.grid = list()
        self.hive = 50, 50
        self.food = {}
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
            self.ants.append(ant())

        for i in range(0, self.food_count):
            l = random.randrange(0, 100)
            m = random.randrange(0, 100)
            while self.grid[l][m] == '1' or self.grid[m][l] == '1':
                l = random.randrange(0, 100)
                m = random.randrange(0, 100)
            self.food[(l, m)] = 100
            self.fd = (l, m)

    def move(self):
        time.sleep(0.1)
        for i in range(0, self.num_of_ants):
            #print "move"
            if len(self.ants[i].path) <= 0:
                if self.food.get((self.ants[i].x, self.ants[i].y), 'a') != 'a':
                    if self.ants[i].mode != 'f':
                        path = self.ants[i].used_path[:]
                        self.ants[i].used_path = list()
                        path.reverse()
                        for j in range(0, len(path)):
                            if path[j][0][0]== self.hive[0] and path[j][0][1] == self.hive[1]:
                                print "b"
                                break
                            self.grid[path[j][0][0]][path[j][0][1]] = 3
                        self.grid[self.ants[i].x][self.ants[i].y] = 0
                        self.grid[self.hive[0]][self.hive[1]] = 0
                    else:
                        if self.ants[i].target == self.fd:
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
                    c = self.food[(self.ants[i].x, self.ants[i].y)]
                    self.food[(self.ants[i].x, self.ants[i].y)] = c - 1

                if self.ants[i].x == self.hive[0] and self.ants[i].y == self.hive[1]:
                    if self.ants[i].mode == 'f':
                        if self.ants[i].target == self.hive:
                            #print "hive"
                            self.ants[i].target = self.fd
                            if len(self.ants[i].pr_path) > 0:
                                for mx_p in self.ants[i].pr_path:
                                    a = self.grid[mx_p[0]][mx_p[1]]
                                    if a < 20:
                                        self.grid[mx_p[0]][mx_p[1]] = a
                                self.ants[i].pr_path = list()
                                self.grid[self.fd[0]][self.fd[1]] = 0
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

                if self.ants[i].mode != 'f' and self.grid[self.ants[i].x][self.ants[i].y] > 0:
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
                            if self.ants[i].x + j >= self.width or self.ants[i].x + j < 0:
                                continue
                            if self.ants[i].y + k >= self.height or self.ants[i].y + k < 0:
                                continue
                            if self.ants[i].x_2 == self.ants[i].x + j and self.ants[i].y_2 == self.ants[i].y + k:
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

                    #print "sss ", i, " ", (x, y), " - ", mx_p
                    self.ants[i].x_2 = self.ants[i].x
                    self.ants[i].y_2 = self.ants[i].y
                    self.ants[i].x = mx_p[0]
                    self.ants[i].y = mx_p[1]
                    #print self.ants[i].x, ", ", self.ants[i].y
                    #print "m"
                    a = self.grid[mx_p[0]][mx_p[1]]
                    if a > 0:
                        #print "mi"
                        self.grid[mx_p[0]][mx_p[1]] = a - 1
                    self.ants[i].pr_path.append(mx_p)

                else:
                    path = self.ants[i].check_trail(self.food, self.grid,
                            self.width, self.height)
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

        for f in self.food.keys():
            if self.food[f] <= 0:
                for i in range(0, self.num_of_ants):
                    self.ants[i].mode = 'r'
                for i in range(0, self.height):
                    for j in range(0, self.width):
                        self.grid[j][i] = 0

                del self.food[f]
                x = random.randrange(0, 100)
                y = random.randrange(0, 100)
                while self.grid[x][y] == '1' or self.grid[y][x] == '1':
                    x = random.randrange(0, 100)
                    y = random.randrange(0, 100)
                self.food[(x, y)] = 100
                self.fd = (x, y)


class ant:

    def __init__(self):
        self.x = 50  # random.randrange(0, 100)
        self.y = 50  # random.randrange(0, 100)
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
        #visited[(sx, sy)] = 0, 0
        while x != dx or y != dy:
            #print x, y
            for j in range(y - 1, y + 2):
                for i in range(x - 1, x + 2):
                    #print dx, dy
                    if j < 0 or i < 0 or i >= w or j >= h:
                        continue
                    if j == y and i == x:
                        continue

                    if visited.get((i, j), 'a') == 'a':
                        #print "i, j = ", i, j
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
                if food.get((i, j), 'a') != 'a':
                    path = self.find_path(self.x, self.y, i, j, grid, w, h)
                    if len(path) != 0:
                        path.reverse()
                        self.with_food = True
                        return path

        if self.count > 5:
            x = random.randrange(-1, 2)  # self.inc_x
            y = random.randrange(-1, 2)  # self.inc_y
            self.count = 0
        else:
            x = self.inc_x
            y = self.inc_y
        f1 = self.x + x >= w or self.y + y >= h
        f2 = self.x + x < 0 or self.y + y < 0
        f3 = x == 0 and y == 0
            #if not (f1 or f2):
                #f3 = grid[self.y + y][self.x + x] == '1'
            #else:
                #f3 = True
        f4 = self.x + x == self.x_2 and self.y + y == self.y_2
        while f1 or f2 or f3 or f4:

            x = random.randrange(-10, 21) / 10
            y = random.randrange(-10, 21) / 10
            f1 = self.x + x >= w or self.y + y >= h
            f2 = self.x + x < 0 or self.y + y < 0
            #if not (f1 or f2):
                #f3 = grid[self.y + y][self.x + x] == '1'
            #else:
                #f3 = True
            f3 = x == 0 and y == 0
            f4 = self.x + x == self.x_2 and self.y + y == self.y_2
            #prnt x, y
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

    def check_trail(self, food, grid, w, h):
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

root = Tk()
root.title("antz")


w = world()
#w.file_read("ab.txt")
cw = 640
ch = 640

chart_1 = Canvas(root, width=cw, height=ch, background="black")
chart_1.grid(row=0, column=0)

while 1:
    w.move()
    for i in range(0, 100):
        for j in range(0, 100):
            p = w.grid[j][i]
            if p > 4:
                p = 4
            if w.grid[j][i] != 0:
                chart_1.create_oval(j * 6 + 20 - p, i * 6 + 20 - p,
                    j * 6 + 20 + p, i * 6 + 20 + p, fill='white')
    for f in w.food.keys():
        c = w.food[f]
        #for i in l:
            #chart_1.create_oval(i[0][0] * 6 + 20 - 2, i[0][1] * 6 + 20 - 2,
                #i[0][0] * 6 + 20 + 2, i[0][1] * 6 + 20 + 2, fill='yellow')
        chart_1.create_oval(f[0] * 6 + 20 - c / 2, f[1] * 6 + 20 - c / 2,
                f[0] * 6 + 20 + c / 2, f[1] * 6 + 20 + c / 2, fill='blue')

    for i in range(0, w.num_of_ants):
        x = w.ants[i].x * 6 + 20
        y = w.ants[i].y * 6 + 20
        if w.ants[i].with_food:
            chart_1.create_oval(x - 5, y - 5,
                    x + 5, y + 5, fill='red')
        else:
            chart_1.create_oval(x - 5, y - 5,
                    x + 5, y + 5, fill='yellow')

    chart_1.create_oval(320 - 6, 320 - 6,
                320 + 6, 320 + 6, fill='red')

    chart_1.update()

    chart_1.delete(ALL)
    #time.sleep(0.1)
root.mainloop()
