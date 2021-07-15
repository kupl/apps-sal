from math import ceil
def growing_plant(u, d, H):
    return ceil(max((H-u)/(u-d), 0))+1
