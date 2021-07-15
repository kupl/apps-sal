from math import ceil

def growing_plant(u, d, h):
    return max(1, min(ceil(h/(u-d)), ceil((h-d)/(u-d))))
