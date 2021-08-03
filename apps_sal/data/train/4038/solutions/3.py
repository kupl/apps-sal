result = (2, 3, 4, 3, 4, 6, 4, 6, 8)


def chess_knight(cell):
    x, y = ord(cell[0]) - 97, int(cell[1]) - 1
    x, y = min(2, x, 7 - x), min(2, y, 7 - y)
    return result[3 * x + y]
