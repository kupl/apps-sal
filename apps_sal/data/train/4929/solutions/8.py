from itertools import count, cycle, takewhile


def get_diagonale_code(grid: str) -> str:
    rows = grid.splitlines()
    it = zip(cycle(rows + rows[-2:0:-1]), count(0, 2))
    chars = (row[c] if c < len(row) else None for (row, c) in it)
    return ''.join(takewhile(lambda c: c, chars))
