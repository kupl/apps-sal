def squares_needed(grains):
    (square, comp) = (0, 0)
    while comp < grains:
        square += 1
        comp += 2 ** (square - 1)
    return square
