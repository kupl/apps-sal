def chess_knight(k):
    (x, y) = (ord(k[0]) - ord('a'), ord(k[1]) - ord('1'))
    moves = 0
    if x - 2 in range(8) and y - 1 in range(8):
        moves += 1
    if x - 2 in range(8) and y + 1 in range(8):
        moves += 1
    if x - 1 in range(8) and y - 2 in range(8):
        moves += 1
    if x - 1 in range(8) and y + 2 in range(8):
        moves += 1
    if x + 1 in range(8) and y - 2 in range(8):
        moves += 1
    if x + 1 in range(8) and y + 2 in range(8):
        moves += 1
    if x + 2 in range(8) and y - 1 in range(8):
        moves += 1
    if x + 2 in range(8) and y + 1 in range(8):
        moves += 1
    return moves
