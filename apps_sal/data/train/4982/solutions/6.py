class Game():

    def __init__(self, board):
        self._board = board
        self._lines = []
        self._flines = []
        self._gboard = []
        self._cboard = []
        self._sqcheck = [(0, 0), (1, -1), (1, 1), (2, 0)]
        self._sqctotal = 0
        self._dot = 0
        self._score = 0
        self._inner = "X"
        self._blank = "_"

        self.createcompleteb()

    def play(self, lines):
        if (lines == []):
            return lines
        self._lines = lines

        creategameb(self, self._lines)

        breaker = False
        lskip = False
        complete = False
        while not complete:
            breaker = False
            lskip = False
            for y in range(len(self._gboard)):
                if (not lskip):
                    lskip = True
                    if(y != len(self._gboard) - 1):
                        for x in range(len(self._gboard)):
                            if(self._gboard[y][x] != self._dot):
                                for sqc in self._sqcheck:
                                    if (self._gboard[y + sqc[0]][x + sqc[1]] != self._blank):
                                        self._sqctotal += 1
                                if(self._sqctotal == 3):
                                    for sqc in self._sqcheck:
                                        if (self._gboard[y + sqc[0]][x + sqc[1]] == self._blank):
                                            self._gboard[y + sqc[0]][x + sqc[1]] = self._cboard[y + sqc[0]][x + sqc[1]]
                                            self._sqctotal = 0
                                            self._score = 1
                                            breaker = True
                                            break

                                elif(self._sqctotal == 4):
                                    self._sqctotal = 0
                                    self._score = 1
                                else:
                                    self._sqctotal = 0
                            else:
                                pass
                    else:
                        complete = True
                else:
                    lskip = False

                if(breaker):
                    breaker = False
                    break

        for y in range(len(self._gboard)):
            for x in range(len(self._gboard)):
                if(isinstance(self._gboard[y][x], int)):
                    if(self._gboard[y][x] > 0):
                        self._flines.append(self._gboard[y][x])

        if(self._score):
            return self._flines
        else:
            return self._lines

    def createcompleteb(self):
        switch = 1
        doi = 0
        count = 1
        tmp = []
        for y in range(self._board + 1 + self._board):
            for x in range(self._board + 1 + self._board):
                if (switch):
                    if (not doi):
                        tmp.append(self._dot)
                        switch = 0
                    else:
                        tmp.append(self._inner)
                        switch = 0
                else:
                    tmp.append(count)
                    count += 1
                    switch = 1
            if(doi == 1):
                doi = 0
            else:
                doi = 1
            self._cboard.append(tmp)
            tmp = []


def creategameb(self, lines):
    switch = 1
    doi = 0
    count = 1
    tmp = []
    for y in range(self._board + 1 + self._board):
        for x in range(self._board + 1 + self._board):
            if (switch):
                if (not doi):
                    tmp.append(self._dot)
                    switch = 0
                else:
                    tmp.append(self._inner)
                    switch = 0
            else:
                if (count in lines):
                    tmp.append(count)
                    count += 1
                    switch = 1
                else:
                    tmp.append(self._blank)
                    count += 1
                    switch = 1

        if(doi == 1):
            doi = 0
        else:
            doi = 1
        self._gboard.append(tmp)
        tmp = []
