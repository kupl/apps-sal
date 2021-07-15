from math import ceil, log

def squares_needed(grains):
    return ceil(log(grains + 1, 2)) if grains else 0
