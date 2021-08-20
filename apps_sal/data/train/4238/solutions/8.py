def squares_needed(grains):
    return 0 if grains == 0 else len(bin(grains)[2:])
