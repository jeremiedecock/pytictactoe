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

from pytictactoe.player.abstract import Player

class HumanPlayer(Player):
    def play(self, game, state):
        game.print_state(state)

        action = None
        while action is None:
            print('Select your square (e.g. "A1"): ', end='')
            input_str = input()

            if (input_str[0].lower() in "abc") and (input_str[1] in "123"):
                if input_str[0].lower() == "a":
                    action = 0
                elif input_str[0].lower() == "b":
                    action = 1
                elif input_str[0].lower() == "c":
                    action = 2

                if input_str[1] == "1":
                    action += 0
                elif input_str[1] == "2":
                    action += 3
                elif input_str[1] == "3":
                    action += 6

                if not game.isValidAction(state, action):
                    action = None
            else:
                action = None

            if action is None:
                print("Wrong value")

        return action
