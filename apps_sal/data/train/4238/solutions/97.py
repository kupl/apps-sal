from math import log, ceil

def squares_needed(grains):
    return ceil(1.4423*log(grains) + 0.0347) if grains else 0
