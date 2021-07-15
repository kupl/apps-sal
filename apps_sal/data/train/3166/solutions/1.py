from math import log

def circle_slash(n):
    return 2 * (n - 2 ** int(log(n, 2))) + 1
