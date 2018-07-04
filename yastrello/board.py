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


class yasTrelloBoard:
    """
    yasTrello Board class.
    """

    def __init__(self, name, conn=None):
        self.name = name
        self.conn = conn
        self.id = None
        self.closed = False
        self.labels = {}
        self.lists = []

        if (conn):
            for board in self._getBoards():
                if board['name'] == self.name:
                    self.id = board['id']
                    self.closed = True if board['closed'] == 'true' else False
                    self.labels = board['labelNames']
                    self.lists = self._getBoardLists()
                    return

            # Create a new Board everytime the id is None
            if (not self.id):
                params = {"name":name}
                ret = json.loads(self.conn.post("/boards/", params))
                if (ret):
                    self.id = ret["id"]
                    self.closed = ret["closed"]
                    self.labels = ret['labelNames']
                    self.lists = self._getBoardLists()
                    return

    def getBoardName(self):
        return self.name

    def getBoardId(self):
        return self.id

    def getBoardLists(self):
        return self.lists

    def getBoardLabels(self):
        return self.labels

    def isBoardClosed(self):
        return self.closed

    def _getBoards(self):
        return json.loads(self.conn.get('/members/me/boards/'))

    def _getBoard(self, id=None):
        if not id:
            return {}

        return json.loads(self.conn.get('/boards/%s' % id))

    def _getBoardLists(self):
        return json.loads(self.conn.get('/boards/%s/lists/' % self.id))


if __name__ == "__main__":
    print
