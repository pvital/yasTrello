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
from card import yasTrelloCard
from conn import yasTrelloConn
from label import yasTrelloLabel
from list import yasTrelloList
from utils import readAPICreds


class yasTrelloApp:
    """
    yasTrello App class.
    """

    def __init__(self, board=None, list=None, card=None, label=None,
                 comment=None):
        cred = readAPICreds()
        self.conn = yasTrelloConn(cred['api_key'], cred['token'])
        self.board = yasTrelloBoard(board, self.conn)

        # Handle label
        self.label = None
        if (label):
            for labelName in self.board.getBoardLabels().values():
                if (labelName == label):
                    # Board already has a label with this name.
                    labelId = self.board.getBoardLabelId(label)
                    if (labelId):
                        self.label = yasTrelloLabel(labelId, label,
                                                    self.board.getBoardId())
                        break
            if (not self.label):
                self.label = yasTrelloLabel(None, label,
                                            self.board.getBoardId(),
                                            'null', self.conn)

        # Based on Board's Lists, we check if one of them matches with the list
        # the user inputed and create our List object here. Otherwise, we
        # create a List on Trello and the List object.
        self.list = None
        for item in self.board.getBoardLists():
            if (item['name'] == list):
                self.list = yasTrelloList(item['id'], item['name'],
                                          item['idBoard'], item['closed'],
                                          self.conn)
                break
        if (not self.list):
            print("No list called \"%s\" was found. Creating..." % list)
            self.list = yasTrelloList(None, list, self.board.getBoardId(),
                                      None, self.conn)

        # Handle Card information
        self.card = None
        for item in self.list.getListCards():
            if (item['name'] == card):
                labelid = self.label.getLabelId() if self.label else None
                self.card = yasTrelloCard(item['id'], item['name'],
                                          item['idBoard'], item['idList'],
                                          item['closed'], labelid, self.conn)
                break
        if (not self.card):
            print("No card exists with this title. Creating...")
            labelid = self.label.getLabelId() if self.label else None
            self.card = yasTrelloCard(None, card, self.board.getBoardId(),
                                      self.list.getListId(), None, labelid,
                                      self.conn)

        # Handle comment
        if (comment):
            self.card.addCommentToCard(comment)

    def getBoard(self):
        return self.board

    def getList(self):
        return self.list

    def getCard(self):
        return self.card


if __name__ == "__main__":
    print
