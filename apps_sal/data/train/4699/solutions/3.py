def spinning_rings(inner_max, outer_max):
    moves, inner, outer = 0, 0, 0

    while True:
        inner -= 1  # decrease inner ring by 1
        inner %= inner_max + 1  # wrap if count goes beyond `inner_max`

        outer += 1  # increase outer ring by 1
        outer %= outer_max + 1  # wrap if count goes beyond `outer_max`

        moves += 1  # count moves

        if(inner == outer):
            break

    return moves
