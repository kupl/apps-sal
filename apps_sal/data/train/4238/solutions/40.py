def squares_needed(grains):
    if not grains:
        return 0
    square = 0
    base = 1
    total = 0
    while total < grains:
        total += base
        base *= 2
        square += 1
    return square
