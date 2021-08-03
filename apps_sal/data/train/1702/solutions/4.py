class Sudoku(object):
    def __init__(self, grid):
        self.grid = grid
        self.dim = len(grid)
        self.boxsize = int(self.dim ** 0.5)
        self.nums = set(range(1, self.dim + 1))

    def row_valid(self, row):
        return self.nums == set(self.grid[row])

    def col_valid(self, col):
        return self.nums == set(self.grid[row][col] for row in range(self.dim))

    def box_valid(self, box):
        box_row, box_col = divmod(box, self.boxsize)
        box_row, box_col = box_row * self.boxsize, box_col * self.boxsize
        return self.nums == set(self.grid[row][col]
                                for row in range(box_row, box_row + self.boxsize)
                                for col in range(box_col, box_col + self.boxsize))

    def is_valid(self):
        if any(len(row) != self.dim for row in self.grid):
            return False
        if any(any(not isinstance(i, int) or i is True or i is False
                   for i in row)
               for row in self.grid):
            return False
        return (all(self.row_valid(row) for row in range(self.dim)) and
            all(self.col_valid(col) for col in range(self.dim)) and
                all(self.box_valid(box) for box in range(self.dim)))
