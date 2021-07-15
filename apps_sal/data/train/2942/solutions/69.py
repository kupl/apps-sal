from math import log2, ceil
def fold_to(distance):
    if 0 > distance: return None
    if distance <= 0.0001: return 0
    return ceil(log2(10000*distance))
