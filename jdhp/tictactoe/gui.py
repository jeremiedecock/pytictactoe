#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# See: http://effbot.org/tkinterbook/canvas.htm

import tkinter as tk

SQUARE_SIZE = 128 # pixels
SQUARE_NUM = 3    # squares per side

def start_button_callback():
    start()

def quit_button_callback():
    quit()

def player1_optionmenu_callback(value):
    print(value)

def player2_optionmenu_callback(value):
    print(value)

root = tk.Tk()

player_list = ["Human",
               "Computer (very easy)"]

player1_label = tk.Label(root, text="Player 1 (X):")
player1_label.grid(row=0, column=0, sticky="w")

player1_var = tk.StringVar()
player1_var.set(player_list[0])
player1_optionmenu = tk.OptionMenu(root, player1_var, *player_list, command=player1_optionmenu_callback)
player1_optionmenu.grid(row=0, column=1, sticky="we")

##

player2_label = tk.Label(root, text="Player 2 (O):")
player2_label.grid(row=1, column=0, sticky="w")

player2_var = tk.StringVar()
player2_var.set(player_list[0])
player2_optionmenu = tk.OptionMenu(root, player2_var, *player_list, command=player2_optionmenu_callback)
player2_optionmenu.grid(row=1, column=1, sticky="we")

##

canvas = tk.Canvas(root,
                   width=SQUARE_NUM*SQUARE_SIZE,
                   height=SQUARE_NUM*SQUARE_SIZE)
canvas.grid(row=2, column=0, columnspan=2, sticky="nswe")

##

# Start / quit / restart button

button = tk.Button(root, text="Start", command=start_button_callback)
button.grid(row=3, column=0, columnspan=2, sticky="we")

for row_index in range(SQUARE_NUM):
    for col_index in range(SQUARE_NUM):
        color = "white"
        tags = ("square", "{}x{}".format(col_index, row_index))

        canvas.create_rectangle(SQUARE_SIZE * col_index,       # x1
                                SQUARE_SIZE * row_index,       # y1
                                SQUARE_SIZE * (col_index + 1), # x2
                                SQUARE_SIZE * (row_index + 1), # y2
                                tag=tags,
                                fill=color,
                                activefill="firebrick3",
                                #activeoutline="firebrick1", # does not work if "width=0"
                                #activewidth=4,              # does not work if "width=0"
                                width=0)

    for col_index in range(1, SQUARE_NUM):
        canvas.create_line((SQUARE_SIZE * col_index, 0, SQUARE_SIZE * col_index, SQUARE_SIZE * SQUARE_NUM),      # coordinates: (x1, y1, x2, y2)
                           fill="black",
                           width=8)

    for row_index in range(1, SQUARE_NUM):
        canvas.create_line((0, SQUARE_SIZE * row_index, SQUARE_SIZE * SQUARE_NUM, SQUARE_SIZE * row_index),      # coordinates: (x1, y1, x2, y2)
                           fill="black",
                           width=8)

# Bind items ##################################################################

def callback(event):               # event is a tkinter.Event object
    id_tuple = canvas.find_withtag("current")  # get the item which is under the mouse cursor

    if len(id_tuple) > 0:
        item_id = id_tuple[0]

        #print(canvas.gettags(item_id))
        item_tag1, item_tag2, item_tag3 = canvas.gettags(item_id)

        print("You have clicked on the square {} (item #{})".format(item_tag2, item_id))
        print([int(coord) for coord in item_tag2.split("x")])
    else:
        raise Exception("Unexpected error")

canvas.tag_bind("square",          # a tag string or an item id
                "<Button-1>",      # the event descriptor
                callback,          # the callback function
                add="+")           # "+" to add this binding to the previous one(s) (i.e. keep the previous binding(s)) or None to replace it or them

###############################################################################

def lock_player_option_menus():
    player1_optionmenu["state"] = "disabled"
    player2_optionmenu["state"] = "disabled"

def unlock_player_option_menus():
    player1_optionmenu["state"] = "normal"
    player2_optionmenu["state"] = "normal"

def lock_grid():
    canvas["state"] = "disabled"

def unlock_grid():
    canvas["state"] = "normal"

def start():
    button["text"] = "Quit"
    button["command"] = quit_button_callback
    lock_player_option_menus()
    unlock_grid()

def quit():
    button["text"] = "Start"
    button["command"] = start_button_callback
    unlock_player_option_menus()
    lock_grid()

# Main loop ###################################################################

quit()
root.mainloop()
