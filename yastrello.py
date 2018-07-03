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

import sys

from yastrello.app import yasTrelloApp


def usage():
    print("""yasTrello - yet another simple Trello app

Usage:
    yastrello <board> <list>
    yastrello -h | --help
    yastrello --version

Options:
    -h --help       Show this message.
    --version       Show version.
""")

def main(argv):
    if len(argv) < 2:
        usage()
        sys.exit(2)
    elif len(argv) == 2:
        if (argv[1] == "-h") or (argv[1] == "--help"):
            usage()
            sys.exit(0)
        elif (argv[1] == "--version"):
            print("yasTrello v0.1")
            sys.exit(0)
        else:
            print("ERROR: Invalid sequence of arguments.")
            print("Usage: yastrello <board> <list>")
            sys.exit(2)

    # Read the arguments to create the card
    app = yasTrelloApp(argv[1], argv[2])
    board = app.getBoard()
    if (not board.getBoardId()):
        print("Using board %s - ID: %s" % (board.getBoardName(),
                                           board.getBoardId()))
    list = app.getList()
    if (not list.getListId()):
        print("Using list %s - ID: %s" % (list.getListName(),
                                          list.getListId()))

if __name__ == "__main__":
    main(sys.argv)
    sys.exit(0)
