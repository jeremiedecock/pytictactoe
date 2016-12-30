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

"""
TODO...
"""

__all__ = ['run']

from jdhp.tictactoe import __version__ as VERSION
from jdhp.tictactoe.game import Game
from jdhp.tictactoe.player.human import HumanPlayer
from jdhp.tictactoe.player.greedy import GreedyPlayer
from jdhp.tictactoe.player.random import RandomPlayer

import argparse
import random
import sys

PLAYER_TYPE_DICT = {"human": HumanPlayer,
                    "greedy": GreedyPlayer,
                    "random": RandomPlayer}

def run():
    """
    TODO...
    """

    # PARSE OPTIONS ###########################################################

    player_type_tuple = tuple(PLAYER_TYPE_DICT)
    available_player_type_str = ", ".join(player_type_tuple[:-1])
    available_player_type_str += " or " + player_type_tuple[-1]

    program_description = "Play the classic Tic-Tac-Toe game " \
                          "using the text-based user interface " \
                          "(mainly intended for AI benchmarks)."
    parser = argparse.ArgumentParser(description=program_description)

    parser.add_argument("--player1", metavar="STRING", default="human",
                        help="define player1 (X): {} (default=human)".format(available_player_type_str))

    parser.add_argument("--player2", metavar="STRING", default="human",
                        help="define player2 (O): {} (default=human)".format(available_player_type_str))

    parser.add_argument("--number", "-n", type=int, default=1, metavar="INTEGER",
                        help="number of games to play (default=1)")

    parser.add_argument("--quiet", "-q", action="store_true",
                        help="quiet mode (don't display game results)")

    parser.add_argument("--version", action="store_true",
                        help="output version information and exit")

    args = parser.parse_args()

    if args.version:
        print(VERSION)
        sys.exit(0)

    player1 = args.player1
    player2 = args.player2
    game_number = args.number
    quiet = args.quiet

    if game_number < 1:
        error_msg = 'The "--number" option should be an integer greater than 0'
        raise ValueError(error_msg)

    # LAUNCH THE GAME #########################################################

    game = Game()

    player_list = [PLAYER_TYPE_DICT[player1]("X"),  # TODO
                   PLAYER_TYPE_DICT[player2]("O")]  # TODO

    for game_index in range(game_number):
        current_player_index = random.randint(0, 1)     # TODO
        current_state = game.getInitialState()

        while not game.isFinal(current_state, player_list):
            current_player = player_list[current_player_index]
            action = current_player.play(game, current_state)
            current_state = game.nextState(current_state, action, current_player)
            current_player_index = (current_player_index + 1) % 2

        if not quiet:
            game.print_state(current_state)

            if game.hasWon(player_list[0], current_state):
                print("Player1 has won!")
            elif game.hasWon(player_list[1], current_state):
                print("Player2 has won!")
            else:
                print("Draw...")

if __name__ == '__main__':
    run()

