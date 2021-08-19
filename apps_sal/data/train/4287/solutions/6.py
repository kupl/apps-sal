def get_participants(h):
    from math import ceil, sqrt
    return ceil(0.5 + sqrt(0.25 + 2 * h))
