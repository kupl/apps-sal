def squares_needed(grains):
    return len(bin(grains)) - 2 if grains != 0 else 0
