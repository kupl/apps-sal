def squares_needed(grains):
    if grains < 1:
        return 0
    else:
        return 1 + squares_needed(grains // 2)
