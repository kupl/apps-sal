def squares_needed(grains):
    i = 0
    while grains:
        grains >>= 1
        i += 1
    return i
