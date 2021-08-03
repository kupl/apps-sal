def squares_needed(grains):
    if grains < 1:
        return 0
    else:
        return squares_needed(grains // 2) + 1
