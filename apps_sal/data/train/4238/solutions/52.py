def squares_needed(grains):
    for i in range(0, 100):
        if 2**i > grains:
            return i
