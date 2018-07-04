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


import json

from board import yasTrelloBoard
from conn import yasTrelloConn
from list import yasTrelloList
from utils import readAPICreds


class yasTrelloApp:
    """
    yasTrello App class.
    """

    def __init__(self, board=None, list=None):
        cred = readAPICreds()
        self.conn = yasTrelloConn(cred['api_key'], cred['token'])
        self.board = yasTrelloBoard(board, self.conn)

        # Based on Board's Lists, we check if one of them matches with the list
        # the user inputed and create our List object here. Otherwise, we
        # create a List on Trello and the List object.
        self.list = None
        for item in self.board.getBoardLists():
            if (item['name'] == list):
                self.list = yasTrelloList(item['id'], item['name'],
                                          item['idBoard'], item['closed'])
                break
        if (not self.list):
            print("No list called \"%s\" was found. Creating..." % list)
            self.list = yasTrelloList(None, list, self.board.getBoardId(),
                                      None, self.conn)

    def getBoard(self):
        return self.board

    def getList(self):
        return self.list


if __name__ == "__main__":
    print
