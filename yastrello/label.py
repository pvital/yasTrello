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


LABEL_COLORS = ['yellow', 'purple', 'blue', 'red', 'green', 'orange',
                'black', 'sky', 'pink', 'lime']

class yasTrelloLabel:
    """
    yasTrello Label class.
    """

    def __init__(self, id, name, idBoard, color=None, conn=None):
        self.conn = conn
        self.id = id
        self.name = name
        self.idBoard = idBoard
        # Check if color inputed is a valid one, otherwise set as null
        self.color = (color if color in LABEL_COLORS else 'null') if color \
                     else 'null'

        # Create a new Label everytime the id is None
        if ((not self.id) and conn):
            params = {"name":name, "idBoard":idBoard, "color": self.color}
            ret = json.loads(self.conn.post("/labels/", params))
            if (ret):
                self.id = ret["id"]
                self.color = ret["color"]

    def getLabelName(self):
        return self.name

    def getLabelId(self):
        return self.id

    def getLabelBoard(self):
        return self.idBoard

    def getLabelColor(self):
        return self.color

    def _getLabel(self, id=None):
        if not id:
            return {}

        if (not self.conn):
            return {}

        return json.loads(self.conn.execute('/labels/%s' % id))


if __name__ == "__main__":
    print
