from math import ceil

def growing_plant(u, d, h):
    return max(1, ceil((h - d) / (u - d)))
