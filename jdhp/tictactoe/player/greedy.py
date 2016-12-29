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

__all__ = ['GreedyPlayer']

import random

from jdhp.tictactoe.player.abstract import Player

class GreedyPlayer(Player):
    """
    TODO...
    """

    def play(self, game, state):
        """
        TODO...
        """
        action_list = game.getSetOfValidActions(state)

        choosen_action = None

        # Choose actions that lead to immediate victory...
        for action in action_list:
            next_state = game.nextState(state, action, self)
            if game.hasWon(self, next_state):
                choosen_action = action
                break

        # ... otherwise choose randomly
        if choosen_action is None:
            #print("randomly choose action")    # debug
            choosen_action = random.choice(action_list)

        return choosen_action
