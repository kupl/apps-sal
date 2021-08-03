def squares_needed(grains):
    n = 0
    while 2**n - 1 < grains:
        n += 1
    return n
