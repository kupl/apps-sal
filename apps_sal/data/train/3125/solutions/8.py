import math


def solve(n):
    d = math.ceil(math.sqrt(n)) - 1
    print(d)
    for a in range(d, 0, -1):
        if n % a == 0:
            e = n / a - a
            print((a, e))
            if e % 2 == 0:
                p = e / 2
                return p * p
    return -1
