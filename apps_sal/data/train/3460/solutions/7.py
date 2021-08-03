from math import factorial


def uniq_count(s):
    s = s.lower()
    n = len(s)
    d = 1
    for c in set(s):
        d *= factorial(s.count(c))
    return factorial(n) // d
