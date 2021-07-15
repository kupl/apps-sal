def chess_knight(cell):
    x, y = (ord(c) - ord(origin) for c, origin in zip(cell, 'a1'))
    return sum(0 <= x + dx < 8 and 0 <= y + dy < 8 for dx, dy in (
        (-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)))
