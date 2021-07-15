from math import ceil

def group_size(S, D):
    return  ceil((0.25 + 2 * D + S * (S - 1))**0.5 - 0.5)
