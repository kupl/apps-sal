import re
import numpy as np

class Nonogram:
    def __init__(self, clues):
        self.clues = clues
        self.possible_rows, self.possible_cols = \
            [[self.possible_cells(len(clues[i]), c) for c in clues[1 - i]] for i in range(2)]

    def possible_cells(self, n, clues):
        if clues == () or clues == (0,):
            return ['0' * n]
        min_width = sum(clues) + len(clues) - 1
        assert min_width <= n
        if len(clues) == 1:
            return [('0' * i + '1' * clues[0]).ljust(n, '0') for i in range(n - clues[0] + 1)]
        res = []
        for i in range(0, n - min_width + 1):
            start = '0' * i + '1' * clues[0] + '0'
            res += [start + p for p in self.possible_cells(n - len(start), clues[1:])]
        return res

    def solve(self):
        w, h = len(self.possible_cols), len(self.possible_rows)
        old_grid, grid = None, '\n'.join(['.' * w] * h)
        while old_grid != grid and grid.find('.') != -1:
            old_grid = grid
            grid = ''.join(self.update_cells(row, p) for row, p in
                           zip(grid.split('\n'), self.possible_rows))
            grid = ''.join(self.update_cells(col, p) for col, p in
                           zip((grid[i:: w] for i in range(w)), self.possible_cols))
            grid = '\n'.join(grid[row:: h] for row in range(h))
        return tuple(tuple(-1 if c == '.' else int(c) for c in r) for r in grid.split('\n'))

    @staticmethod
    def update_cells(cells, possibilities):
        if cells.find('.') == -1:
            return cells
        not_matches = [i for i, answer in enumerate(possibilities) if not re.match(cells, answer)]
        for i in not_matches[:: -1]:
            possibilities.pop(i)
        assert len(possibilities) != 0
        if len(possibilities) == 1:
            return possibilities[0]
        n, stack = len(cells), ''.join(possibilities)
        vote = (set(stack[i:: n]) for i in range(0, n))
        return ''.join(s.pop() if len(s) == 1 else '.' for s in vote)
