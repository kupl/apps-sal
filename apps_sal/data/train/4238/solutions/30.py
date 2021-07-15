def squares_needed(grains):
    return 0 if grains < 1 else 1 + squares_needed(grains // 2)
