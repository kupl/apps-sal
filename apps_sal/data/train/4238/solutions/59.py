def squares_needed(grains):
    if grains == 0:
        return 0
    square = 1
    grain_in_square = 1
    total_grains = 1
    while grains > total_grains:
        square += 1
        grain_in_square *= 2
        total_grains += grain_in_square
    return square
