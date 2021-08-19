def spinning_rings(inner_max, outer_max):
    (moves, inner, outer) = (0, 0, 0)
    while True:
        inner -= 1
        inner %= inner_max + 1
        outer += 1
        outer %= outer_max + 1
        moves += 1
        if inner == outer:
            break
    return moves
