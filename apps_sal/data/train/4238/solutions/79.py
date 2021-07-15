def squares_needed(grains, squares=0):
    if grains == 0:
        return 0
    while grains >= 2<<squares :
        squares += 1
    return squares+1

