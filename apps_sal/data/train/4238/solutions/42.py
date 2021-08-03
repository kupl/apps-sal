def squares_needed(grains):
    sm, i = grains, 0
    while sm > 0:
        sm -= 2 ** i
        i += 1
    return i
