import numpy as np


class Sudoku(object):

    def __init__(self, theArray):
        self.grid = np.array(theArray)
        self.listgrid = theArray
        self.N = len(theArray)
        self.M = len(theArray[0])

    def has_valid_size(self):
        if isinstance(self.listgrid[0][0], bool):
            return False
        if self.grid.shape == (1, 1):
            return True
        for i in self.listgrid:
            if len(i) != self.N:
                return False
        return True

    def is_valid(self):
        if not self.has_valid_size():
            return False
        seqs2check = [self.getRowsIterator(), self.getColsIterator(), self.getSquaresIterator()]
        for it in seqs2check:
            for seq in it:
                if self.checkSeq(seq) == False:
                    return False
        return True

    def getRowsIterator(self):
        for i in range(self.N):
            yield self.grid[i, :]

    def getColsIterator(self):
        for i in range(self.N):
            yield self.grid[:, i]

    def getSquaresIterator(self):
        squareSize = int(np.sqrt(self.N))
        for i in range(squareSize):
            for j in range(squareSize):
                ix1 = i * squareSize
                ix2 = j * squareSize
                yield self.grid[ix1:ix1 + squareSize, ix2:ix2 + squareSize].flatten()

    def checkSeq(self, seq):
        return sorted(seq) == list(range(1, self.N + 1))
