def tower_of_hanoi(rings):
    moves = 0
    for r in range(rings):
        moves *= 2
        moves += 1
    return moves



