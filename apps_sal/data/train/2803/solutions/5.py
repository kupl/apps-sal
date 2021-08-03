from math import gcd


def DPC_sequence(s):
    r = 1
    pset = set()
    for i, c in enumerate(s):
        x = i + 1
        if c == 'D':
            if r % x == 0:
                continue
            y = x // gcd(r, x)
            if y in pset:
                return-1
            r *= y
        elif c == 'P':
            if r % x == 0 or gcd(r, x) > 1:
                return -1
            pset.add(x)
        else:
            if r % x == 0 or gcd(r, x) == 1:
                return -1
    return r
