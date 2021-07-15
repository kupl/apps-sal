from functools import cmp_to_key

def comp(x, y):
    rx, ry = x&1, y&1
    while rx == ry:
        x, y = (x - rx) >> 1, (y - ry) >> 1
        rx, ry = x&1, y&1
    return rx > ry

def oddest(a):
    return max(a, key=cmp_to_key(comp))
