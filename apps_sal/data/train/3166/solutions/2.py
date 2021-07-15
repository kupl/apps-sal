from math import log2
def circle_slash(n):
    m = 2 ** int(log2(n))
    return n % m * 2 + 1
