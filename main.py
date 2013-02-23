#!/usr/bin/env python

"""
Author : tharindra galahena (inf0_warri0r)
Project: ant colony simulation
Blog   : http://www.inf0warri0r.blogspot.com
Date   : 22/02/2013
License:

     Copyright 2013 Tharindra Galahena

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

from Tkinter import *
import antz
import time


root = Tk()
root.title("ant colony simulation")
w = antz.world()
cw = 640
ch = 640

chart_1 = Canvas(root, width=cw, height=ch, background="green")
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

    c = w.food_amount
    f = w.food
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

    chart_1.create_oval(320 - 12, 320 - 12,
                320 + 12, 320 + 12, fill='red')

    chart_1.update()

    chart_1.delete(ALL)
    time.sleep(0.1)
root.mainloop()
