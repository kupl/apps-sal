def squares_needed(grains):
    if grains == 0:
        return 0
    i = 0
    while (2**i - 1) // grains < 1:
        i += 1
    return i
