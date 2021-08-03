from math import ceil
def growing_plant(u, d, h): return max([ceil((h - u) / (u - d)), 0]) + 1
