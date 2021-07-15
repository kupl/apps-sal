moves = {(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)}
def chess_knight(cell):
    x, y = ord(cell[0]) - ord('a') + 1, int(cell[1])
    return sum(0 < x + mx < 9 and 0 < y + my < 9 for mx, my in moves)
