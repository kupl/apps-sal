from math import log2, ceil


def fold_to(d):
    return ceil(log2(d / 0.0001)) if d > 0.0001 else None if d < 0 else 0
