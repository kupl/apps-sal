from string import ascii_lowercase

_MOVES = [complex(a * c, b * d) for a, b in ((1, 2), (2, 1)) for c in (1, -1) for d in (1, -1)]
_BOARD = [complex(a, b) for a in range(1, 9) for b in range(1, 9)]

def chess_knight(cell):
    file, rank = cell
    start = complex(ascii_lowercase.index(file) + 1, int(rank))
    return sum(start + move in _BOARD for move in _MOVES)

