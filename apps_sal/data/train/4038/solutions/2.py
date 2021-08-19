def chess_knight(cell):
    (x, y) = (ord(cell[0]) - 96, int(cell[1]))
    return sum([1 for dx in [-2, -1, 1, 2] for dy in [-2, -1, 1, 2] if all([abs(dx / dy) != 1, 0 < x + dx < 9, 0 < y + dy < 9])])
