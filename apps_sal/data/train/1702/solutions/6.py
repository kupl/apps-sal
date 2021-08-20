class Sudoku(object):

    def __init__(self, board):
        self.board = board

    def is_valid(self):
        n = int(len(self.board) ** 0.5)
        if not all((len(row) == n * n and all((not isinstance(cell, bool) for cell in row)) for row in self.board)):
            return False
        (r, rr) = (range(n), range(0, n * n, n))
        blocks = [[self.board[x + a][y + b] for a in r for b in r] for x in rr for y in rr]
        return not [x for x in self.board + list(zip(*self.board)) + blocks if set(x) != set(range(1, n * n + 1))]
