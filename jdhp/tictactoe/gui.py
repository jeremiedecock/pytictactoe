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

"""
TODO...
"""

__all__ = ['TkGUI']

from jdhp.tictactoe.game import Game
from jdhp.tictactoe.player.random import RandomPlayer
from jdhp.tictactoe.player.human import HumanPlayer

import tkinter as tk

SQUARE_SIZE = 128 # pixels
SQUARE_NUM = 3    # squares per side

class TkGUI:
    """
    TODO...
    """

    def __init__(self):
        """
        TODO...
        """

        # Game attributes #############

        self.game = Game()
        self.player_list = None
        self.current_player_index = None
        self.current_state = None

        # GUI parameters ##############

        # TODO...

        # Make the main window ########

        self.root = tk.Tk()                # TODO
        self.root.resizable(False, False)  # <- Lock the size of the window

        # Make widgets ################

        self.available_player_type_list = ["Human",
                                           "Computer (very easy)"]

        # Player1 option menu
        player1_label = tk.Label(self.root, text="Player 1 (X):")
        player1_label.grid(row=0, column=0, sticky="w")

        self._player1_var = tk.StringVar()
        self._player1_var.set(self.available_player_type_list[0])
        self.player1_optionmenu = tk.OptionMenu(self.root,
                                           self._player1_var,
                                           *self.available_player_type_list)
                                           #command=self.set_player1)
        self.player1_optionmenu.grid(row=0, column=1, sticky="we")

        # Player2 option menu
        player2_label = tk.Label(self.root, text="Player 2 (O):")
        player2_label.grid(row=1, column=0, sticky="w")

        self._player2_var = tk.StringVar()
        self._player2_var.set(self.available_player_type_list[0])
        self.player2_optionmenu = tk.OptionMenu(self.root,
                                           self._player2_var,
                                           *self.available_player_type_list)
                                           #command=self.set_player2)
        self.player2_optionmenu.grid(row=1, column=1, sticky="we")

        # Canvas
        self.canvas = tk.Canvas(self.root,
                                width=SQUARE_NUM*SQUARE_SIZE,
                                height=SQUARE_NUM*SQUARE_SIZE)
        self.canvas.grid(row=2, column=0, columnspan=2, sticky="nswe")

        self.canvas.tag_bind("square",             # a tag string or an item id
                             "<Button-1>",         # the event descriptor
                             self.canvas_callback, # the callback function
                             add="+")              # "+" to add this binding to the previous one(s) (i.e. keep the previous binding(s)) or None to replace it or them

        # Start / Quit / Restart button
        self.button = tk.Button(self.root, text="Start")
        self.button.grid(row=3, column=0, columnspan=2, sticky="we")

    ###################################

    def run(self):
        """
        TODO...
        """
        # Tk event loop
        # TODO ???
        self.init()
        self.root.mainloop()

    ###################################

    def init(self):
        """
        TODO...
        """
        self.player_list = None          # TODO
        self.current_player_index = None # TODO
        self.current_state = None        # TODO

        self.draw_current_state()

        self.button["text"] = "Start"
        self.button["command"] = self.start
        self.unlock_player_option_menus()
        self.lock_grid()

    def start(self):
        """
        TODO...
        """
        self.button["text"] = "Quit"
        self.button["command"] = self.init
        self.lock_player_option_menus()
        self.unlock_grid()

    def lock_player_option_menus(self):
        """
        TODO...
        """
        self.player1_optionmenu["state"] = "disabled"
        self.player2_optionmenu["state"] = "disabled"

    def unlock_player_option_menus(self):
        """
        TODO...
        """
        self.player1_optionmenu["state"] = "normal"
        self.player2_optionmenu["state"] = "normal"

    def lock_grid(self):
        """
        TODO...
        """
        self.canvas["state"] = "disabled"

    def unlock_grid(self):
        """
        TODO...
        """
        self.canvas["state"] = "normal"

    ###################################

    def get_player1_type(self):
        """
        TODO...
        """
        return self._player1_var.get()

    def get_player2_type(self):
        """
        TODO...
        """
        return self._player2_var.get()

    ###################################

    def canvas_callback(self, event):                   # event is a tkinter.Event object
        """
        TODO...
        """
        id_tuple = self.canvas.find_withtag("current")  # get the item which is under the mouse cursor

        if len(id_tuple) > 0:
            item_id = id_tuple[0]

            #print(self.canvas.gettags(item_id))
            item_tag1, item_tag2, item_tag3 = self.canvas.gettags(item_id)

            print("You have clicked on the square {} (item #{})".format(item_tag2, item_id))
            print([int(coord) for coord in item_tag2.split("x")])
        else:
            raise Exception("Unexpected error")

    def draw_current_state(self):
        """
        TODO...
        """
        for row_index in range(SQUARE_NUM):
            for col_index in range(SQUARE_NUM):
                color = "white"
                tags = ("square", "{}x{}".format(col_index, row_index))

                self.canvas.create_rectangle(SQUARE_SIZE * col_index,       # x1
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
                self.canvas.create_line((SQUARE_SIZE * col_index, 0, SQUARE_SIZE * col_index, SQUARE_SIZE * SQUARE_NUM),      # coordinates: (x1, y1, x2, y2)
                                   fill="black",
                                   width=8)

            for row_index in range(1, SQUARE_NUM):
                self.canvas.create_line((0, SQUARE_SIZE * row_index, SQUARE_SIZE * SQUARE_NUM, SQUARE_SIZE * row_index),      # coordinates: (x1, y1, x2, y2)
                                   fill="black",
                                   width=8)

if __name__ == '__main__':
    gui = TkGUI()

    # Launch the main loop
    gui.run()

