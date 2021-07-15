from itertools import count

def folding(a, b):
    for c in count(0):
        if a == 1: return c + b
        if b == 1: return c + a
        if a == b: return c + 1
        a, b = abs(a-b), min(a, b)
