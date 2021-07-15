from math import log2

def squares_needed(grains):
    return 0 if not grains else int(log2(grains)) + 1
