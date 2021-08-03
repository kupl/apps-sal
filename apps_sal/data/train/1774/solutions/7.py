from typing import Tuple


class Funnel:
    def __init__(self):
        self.arr = [[None] * (i + 1) for i in reversed(list(range(5)))]

    def __getitem__(self, indexes: Tuple[int, int]):
        r, c = indexes
        if 0 <= r < 5 and 0 <= c < (5 - r):
            return self.arr[r][c]

    def fill(self, *args):
        args = [*args]
        for row in reversed(self.arr):
            for i, x in enumerate(row):
                if args and x is None:
                    row[i] = args.pop(0)

    def above(self, r: int, c: int):
        if r >= 0 and c >= 0 and self[r, c] is not None:
            yield r, c

            for d in range(2):
                if self[r - 1, c + d] is not None:
                    yield r - 1, c + d
                    yield from self.above(r - 1, c + d)

    def drip(self, row: int = 4, col: int = 0):
        if row >= 0:
            left, right = (len({*self.above(row - 1, col + d)}) for d in range(2))
            self.arr[row][col], val = self.drip(row - 1, col + (right > left)), self.arr[row][col]
            return val

    def __str__(self):
        return '\n'.join(
            ' ' * i + fr"\{' '.join(' ' if x is None else str(x) for x in row)}/"
            for i, row in enumerate(self.arr)
        )
