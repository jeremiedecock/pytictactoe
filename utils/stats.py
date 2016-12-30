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

import argparse
import json

def main():
    """TODO..."""

    # PARSE OPTIONS ###########################################################

    parser = argparse.ArgumentParser(description="Make statistics on results files (JSON files).")

    parser.add_argument("fileargs", nargs=1, metavar="FILE",
                        help="The JSON file to process")

    args = parser.parse_args()

    json_file_path = args.fileargs[0]

    # PARSE THE RESULTS FILES #################################################

    with open(json_file_path, "r") as fd:
        data = json.load(fd)

    result_list = [game["winner"]for game in data["game_log_list"]]
    print("player1: {} ({:.2f}%)".format(result_list.count(0), 100. * result_list.count(0)/len(result_list)))
    print("player2: {} ({:.2f}%)".format(result_list.count(1), 100. * result_list.count(1)/len(result_list)))
    print("draw: {} ({:.2f}%)".format(result_list.count(None), 100. * result_list.count(None)/len(result_list)))

if __name__ == '__main__':
    main()
