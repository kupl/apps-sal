def possible_positions(pos):
    board = [[r + str(c) for c in range(1, 9)] for r in 'abcdefgh']
    (x, y) = (ord(pos[0]) - 97, int(pos[1]) - 1)
    return sorted([board[py][px] for (py, px) in [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)] if 0 <= px < 8 and 0 <= py < 8])
