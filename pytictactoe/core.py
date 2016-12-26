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

import random

class Player:
    def __init__(self, player_type, symbol):
        self.player_type = player_type
        self.symbol = symbol

    def play(self, game, state):
        raise NotImplementedError()

class HumanPlayer(Player):
    def play(self, game, state):
        print_state(state)

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

class RandomPlayer(Player):
    def play(self, game, state):
        action = random.choice(game.getSetOfValidActions(state))
        return action

###############################################################################

class Game:
    def getSetOfValidActions(self, state):
        # Get the list index of empty squares
        list_of_valid_actions = [index for index,symbol in enumerate(state) if symbol==" "]

        return list_of_valid_actions 

    def nextState(self, state, action, player):
        if not self.isValidState(state):
            raise Exception(ValueError("Wrong state value:", state))

        if not self.isValidAction(state, action):
            raise Exception(ValueError("Wrong state value:", state))

        state[action] = player.symbol

        return state

    def isFinal(self, state, player_list):
        if not self.isValidState(state):
            raise Exception(ValueError("Wrong state value:", state))

        is_final = False

        # Check if there is at least one empty square
        if state.count(" ") == 0 or self.hasWon(player_list[0], state) or self.hasWon(player_list[1], state):
            is_final = True

        return is_final

    def hasWon(self, player, state):
        if not self.isValidState(state):
            raise Exception(ValueError("Wrong state value:", state))

        state_mask = [1 if value==player.symbol else 0 for value in state]

        has_won = False

        # Check lines
        if sum(state_mask[0:3])==3 or sum(state_mask[3:6])==3 or sum(state_mask[6:9])==3:
            has_won = True

        # Check columns
        elif sum(state_mask[0:9:3])==3 or sum(state_mask[1:9:3])==3 or sum(state_mask[2:9:3])==3:
            has_won = True

        # Check diagonals
        elif sum(state_mask[0:9:4])==3 or sum(state_mask[2:7:2])==3:
            has_won = True

        return has_won

    def isValidState(self, state):
        is_valid = True

        try:
            if len(state) == 9:
                for square_value in state:
                    if square_value not in [" ", "X", "O"]:
                        is_valid = False
                        break
            else:
                is_valid = False
        except:
            is_valid = False

        return is_valid

    def isValidAction(self, state, action):
        return (action in range(9)) and (state[action] == " ")


def print_state(state):
    print("  A B C")
    print(" +-+-+-+")
    print("3|{}|{}|{}|3".format(state[6], state[7], state[8]))
    print(" +-+-+-+")
    print("2|{}|{}|{}|2".format(state[3], state[4], state[5]))
    print(" +-+-+-+")
    print("1|{}|{}|{}|1".format(state[0], state[1], state[2]))
    print(" +-+-+-+")
    print("  A B C")


game = Game()

player_list = [HumanPlayer("human", "X"), RandomPlayer("random", "O")]
current_player_index = 0
current_state = [" "] * 9

while not game.isFinal(current_state, player_list):
    current_player = player_list[current_player_index]
    action = current_player.play(game, current_state)
    current_state = game.nextState(current_state, action, current_player)
    current_player_index = (current_player_index + 1) % 2

print_state(current_state)     # Optionnal, should be moved in player.play for human players only

if game.hasWon(player_list[0], current_state):
    print("Player1 has won!")
elif game.hasWon(player_list[1], current_state):
    print("Player2 has won!")
else:
    print("Draw...")

