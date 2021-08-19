def squares_needed(grains):
    return 1 + squares_needed(grains >> 1) if grains else 0
