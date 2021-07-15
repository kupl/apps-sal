from math import log2, ceil

def squares_needed(grains):
    return grains and ceil(log2(grains+1))
