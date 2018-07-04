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


class yasTrelloList:
    """
    yasTrello List class.
    """

    def __init__(self, id, name, idBoard, closed, conn=None):
        self.id = id
        self.name = name
        self.closed = closed
        self.idBoard = idBoard
        self.conn = conn
        self.cards = self._getListCards() if (conn and self.id) else []
        # Create a new List everytime the id is None
        if ((not self.id) and conn):
            params = {"name":name, "idBoard":idBoard}
            ret = json.loads(self.conn.post("/lists/", params))
            if (ret):
                self.id = ret["id"]
                self.closed = ret["closed"]
                self.cards = self._getListCards()

    def getListName(self):
        return self.name

    def getListId(self):
        return self.id

    def getListBoard(self):
        return self.idBoard

    def getListCards(self):
        return self.cards

    def isListClosed(self):
        return self.closed

    def _getList(self, id=None):
        if not id:
            return {}

        if (not self.conn):
            return {}

        return json.loads(self.conn.get('/lists/%s' % id))

    def _getListCards(self):
        return json.loads(self.conn.get('/lists/%s/cards/' % self.id))


if __name__ == "__main__":
    print
