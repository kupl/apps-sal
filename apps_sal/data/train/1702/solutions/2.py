import math


class Sudoku(object):

    def __init__(self, board):
        self.board = board
        self.size = len(board)

    @staticmethod
    def reduce_logic(seq):
        return reduce(lambda x, y: x and y, seq)

    def is_square(self):
        return self.reduce_logic(map(lambda x: len(x) == self.size, self.board))

    def check_number(self):
        return self.reduce_logic(map(lambda x: 0 < x <= self.size and type(x) == type(1), reduce(lambda x, y: x + y, self.board)))

    def check_seq(self, seq):
        return self.reduce_logic(map(lambda x: len(set(x)) == self.size, seq))

    def check_rows(self):
        return self.check_seq(self.board)

    def check_cols(self):
        cols = [map(lambda x: x[i], self.board) for i in range(self.size)]
        return self.check_seq(cols)

    def check_little_squares(self):
        sq = int(math.sqrt(self.size))
        squares = [reduce(lambda x, y: x + y, map(lambda x: x[i:i + sq], self.board[j:j + sq])) for j in range(0, self.size, sq) for i in range(0, self.size, sq)]
        return self.check_seq(squares)

    def is_valid(self):
        if self.is_square() and self.check_number() and self.check_rows() and self.check_cols() and self.check_little_squares():
            return True
        else:
            return False
