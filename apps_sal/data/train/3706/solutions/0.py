from math import ceil, sqrt

def layers(n):
    return ceil(sqrt(n)) // 2 + 1
