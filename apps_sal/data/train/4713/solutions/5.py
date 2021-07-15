from itertools import permutations

def late_clock(digits):
    return "{}{}:{}{}".format(*max(c for c in permutations(digits) if c[:2] < (2,4) and c[2:] < (6,0)))
