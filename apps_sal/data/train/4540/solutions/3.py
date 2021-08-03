import random


def prime_or_composite(q, k=100):
    q = abs(q)
    if q == 2:
        return 'Probable Prime'
    if q < 2 or q & 1 == 0:
        return 'Composite'

    d = (q - 1) >> 1
    while d & 1 == 0:
        d >>= 1
    for i in range(k):
        a = random.randint(1, q - 1)
        t = d
        y = pow(a, t, q)
        while t != q - 1 and y != 1 and y != q - 1:
            y = pow(y, 2, q)
            t <<= 1
        if y != q - 1 and t & 1 == 0:
            return 'Composite'
    return 'Probable Prime'
