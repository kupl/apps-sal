from math import log2
from math import ceil

def squares_needed(grains):
    return 0 if not grains else ceil(log2(grains+1))
