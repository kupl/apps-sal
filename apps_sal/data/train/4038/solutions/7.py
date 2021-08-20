def chess_knight(cell):
    (col, row) = cell
    (col, row) = (ord(col) - 97, int(row) - 1)
    return sum((abs(y - row) ** 2 + abs(x - col) ** 2 == 5 for y in range(8) for x in range(8)))
