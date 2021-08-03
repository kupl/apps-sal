def squares_needed(grains):
    return 1 + squares_needed(grains // 2) if grains else 0
