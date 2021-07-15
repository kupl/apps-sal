import math

def group_size(S, D):
    return math.ceil(((-1 +(1 - 4 * S + 4 * S ** 2 + 8 * D) ** 0.5) / 2))

