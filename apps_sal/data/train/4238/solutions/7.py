def squares_needed(grains):
    if not grains:
        return grains
    squares = 1
    while 2 ** squares <= grains:
        squares += 1
    return squares
