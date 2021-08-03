def squares_needed(grains):
    if grains == 0:
        return 0
    else:
        for i in range(1, 65):
            if grains < 2**i:
                return i
