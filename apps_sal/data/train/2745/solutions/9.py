def tower_of_hanoi(rings):
    moves = 7
    r = 3
    while r < rings:
        moves = (moves * 2) + 1
        r += 1
    return moves
