import math


class Sudoku(object):
    def __init__(self, board):
        self.board = board
        self.size = len(board)
        self.lil_size = math.sqrt(self.size)

    def is_valid(self):
        if not all(len(r) == self.size for r in self.rows()):
            return False

        if not self.lil_size.is_integer():
            return False

        if self.board[0][0] is True:
            return False

        numbers = range(1, self.size + 1)
        groups = self.rows() + self.columns() + self.lil_squares()
        for group in groups:
            if sorted(group) != numbers:
                return False

        return True

    def rows(self):
        return self.board

    def columns(self):
        return zip(*self.rows())

    def lil_squares(self):
        result = []
        size = int(self.lil_size)
        for i in range(size):
            for j in range(size):
                square = []
                for k in range(size):
                    for l in range(size):
                        square.append(self.board[i * size + k][j * size + l])
                result.append(square)
        return result
