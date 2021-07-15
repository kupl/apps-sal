from collections import Counter

def solve(*args):
    c1, c2 = map(Counter, args)
    return 2 - any(c1[k]-c2[k] >= 2 and k not in c2 for k in c1)
