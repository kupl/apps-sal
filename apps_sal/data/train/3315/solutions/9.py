from math import log
from math import floor


def strongest_even(n, m):
    a = 2**floor(log(m) / log(2))
    b = 1
    while a * b < n or a * b > m:
        a /= 2
        b += 2
        while a * b <= m:
            if a * b >= n:
                return a * b
            b += 2

    return a * b
# strongest_even(33,47)
