def squares_needed(grains):
    if grains == 0:
        return grains
    total = 0
    for i in range(0, 65):
        total += 2 ** i
        if grains <= total:
            return i + 1
