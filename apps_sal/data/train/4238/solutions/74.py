def squares_needed(grains):
    counter = 0
    if grains == 0:
        return 0
    if grains == 1:
        return 1
    for square in range(1, 64 + 1):
        while grains > 0:
            counter += 1
            grains = grains // 2
    return counter
