#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2012 Jérémie DECOCK (http://www.jdhp.org)

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

import os
import sys

symbols = {-1: "x", 0: " ", 1: "o"}

dot_node_declaration = []
dot_edge_declaration = []

class Node:
    """Node class"""

    id_count = 0     # Used for the graphviz representation of the tree

    def __init__(self, value):
        self._value = tuple(value)
        self._id = Node.id_count
        Node.id_count += 1

    def getValue(self):
        return self._value

    def getChildNodes(self):
        child_nodes = []

        if not self.isFinal():
            player_id = self._value[-1]

            # Get the list index of empty squares (that is to say self._value[index]==0)
            empty_indices = [index for index, value in enumerate(self._value[:-1]) if value==0]
            for index in empty_indices:
                child_node_value = list(self._value)  # *copy* the list
                child_node_value[index] = player_id
                child_node_value[-1] = player_id * -1
                
                child_nodes.append(Node(child_node_value))

        return child_nodes

    def isFinal(self):
        is_final = False

        value = self._value[0:9]

        # Check if there is at least one empty square
        if value.count(0) == 0:
            is_final = True

        # Check lines
        elif abs(sum(value[0:3]))==3 or abs(sum(value[3:6]))==3 or abs(sum(value[6:9]))==3:
            is_final = True

        # Check columns
        elif abs(sum(value[0:9:3]))==3 or abs(sum(value[1:9:3]))==3 or abs(sum(value[2:9:3]))==3:
            is_final = True

        # Check diagonals
        elif abs(sum(value[0:9:4]))==3 or abs(sum(value[2:7:2]))==3:
            is_final = True

        return is_final


def walk(node):
    """The tree traversal function"""

    # Do something with node value...
    str_val = [symbols[item] for item in node.getValue()[0:9]]       # convert node.value (list of integers) to list of string (tictactoe symbols "x", " " and "o")

    # Graphviz
    dot_node_declaration.append('\t%d [shape=record, label="{%s}|{%s}|{%s}"];' % (node._id, "|".join(str_val[0:3]), "|".join(str_val[3:6]), "|".join(str_val[6:9])))

    # Recurse on each child node
    for child_node in node.getChildNodes():
        walk(child_node)

        # Graphviz
        dot_edge_declaration.append('\t%d -> %d;' % (node._id, child_node._id))


def main():
    """Main function

    Build the tic-tac-toe game tree and traverse it.
    """

    # Build the game tree
    #root = Node([0, 0, 0,  0, 0, 0,  0, 0, 0,  1])
    #root = Node([1, 0, 1,  -1, 0, -1,  1, -1, 0,  1])
    root = Node([0, 0, 1,  0, 0, -1,  1, -1, 0,  1])

    # Traverse the tree
    walk(root)

    # Print the "dot" (Graphviz) representation of the tree
    print "digraph G {"
    print os.linesep.join(dot_node_declaration)
    print os.linesep.join(dot_edge_declaration)
    print "}"

    # Print some statistics about the tree
    print >> sys.stderr, len(dot_node_declaration), "nodes generated"
    print >> sys.stderr, len(dot_edge_declaration), "edges generated"

if __name__ == '__main__':
    main()

