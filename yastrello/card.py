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

from conn import yasTrelloConn


class yasTrelloCard:
    """
    yasTrello Card class.
    """

    def __init__(self, id, name, idBoard, idList, closed, idLabel=None,
                 conn=None):
        self.conn = conn
        self.id = id
        self.name = name
        self.closed = closed
        self.idBoard = idBoard
        self.idList = idList
        self.idLabels = self._getIdLabels()['idLabels']
        # Create a new Card everytime the id is None
        if ((not self.id) and conn):
            params = {"name":name, "idList":idList}
            ret = json.loads(self.conn.post("/cards/", params))
            if (ret):
                self.id = ret["id"]
                self.closed = ret["closed"]
        # Add label to the card is inputed
        if (idLabel) and (idLabel not in self.idLabels):
            self.idLabels.append(self.addLabelToCard(idLabel))

    def getCardName(self):
        return self.name

    def getCardId(self):
        return self.id

    def getCardBoard(self):
        return self.idBoard

    def getCardList(self):
        return self.idList

    def isCardClosed(self):
        return self.closed

    def _getCard(self, id=None):
        if not id:
            return {}

        if (not self.conn):
            return {}

        return json.loads(self.conn.get('/cards/%s' % id))

    def _getIdLabels(self):
        return json.loads(self.conn.get('/cards/%s?fields=idLabels' % self.id))

    def addLabelToCard(self, idLabel):
        params = {"value": idLabel}
        ret = json.loads(self.conn.post('/cards/%s/idLabels/' % self.id,
                                         params))
        if (ret):
            return ret[0]

    def addCommentToCard(self, comment):
        params = {"text": comment}
        ret = json.loads(self.conn.post('/cards/%s/actions/comments/' % self.id,
                                         params))
        if (ret):
            return ret


if __name__ == "__main__":
    print
