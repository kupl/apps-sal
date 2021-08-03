def squares_needed(grains):
    if grains == 0:
        return 0
    return squares_needed(grains // 2) + 1
