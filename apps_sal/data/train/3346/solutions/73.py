import math

def prime(x):
    if not (any(not (x%y) for y in range(2, int(math.ceil(math.sqrt(x))) + 1))):
        return True

def gap(g, m, n):
    prev = None
    for curr in range(m, n + 1):
        if prime(curr):
            if curr - (prev or curr) == g:
                return [prev, curr]
            else:
                prev = curr

