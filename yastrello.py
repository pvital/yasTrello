#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2018 Paulo Vital
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import getopt
import sys

from yastrello.app import yasTrelloApp


def usage():
    print("""yasTrello - yet another simple Trello app

Usage:
    yastrello -b <board> -l <list> -c <card_title_between_quotes>
    yastrello -h | --help
    yastrello --version

Options:
    -b --board      Board name to use.
    -l --list       List name to use in the specified Board.
    -c --card       Card title (name) to create in the specified List.
    -h --help       Show this message.
    --version       Show version.
""")

def main(argv):
    if len(argv) < 2:
        usage()
        sys.exit(2)
    else:
        board = None
        list = None
        card = None
        # Process the arguments from command line
        long_opts = ["board=", "list=", "card=", "help", "version"]
        options, remainder = getopt.getopt(sys.argv[1:], "hb:l:c:", long_opts)
        for opt, arg in options:
            if opt in ("-b", "--board"):
                board = arg
            if opt in ("-l", "--list"):
                list = arg
            if opt in ("-c", "--card"):
                card = arg
            elif opt in ("-h", "--help"):
                usage()
                sys.exit(0)
            elif opt == "--version":
                print("yasTrello v0.1")
                sys.exit(0)

    # Read the arguments to create the card
    if ((not board) or (not list) or (not card)):
        print("ERROR: missing arguments.")
        usage()
        sys.exit(2)

    app = yasTrelloApp(board, list)
    board = app.getBoard()
    if (board.getBoardId()):
        print("Using board %s - ID: %s" % (board.getBoardName(),
                                           board.getBoardId()))
    list = app.getList()
    if (list.getListId()):
        print("Using list %s - ID: %s" % (list.getListName(),
                                          list.getListId()))

    print("Using card %s - ID: %s" % (card, None))

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
