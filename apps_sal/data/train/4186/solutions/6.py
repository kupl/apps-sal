from math import log


def sum_of_threes(n):
    out = []
    while n > 0:
        next = int(log(n, 3))
        next += 1 if pow(3, next + 1) <= n else 0
        if out and next == out[-1]:
            return 'Impossible'
        out.append(next)
        n -= pow(3, next)
    return '+'.join(('3^{}'.format(i) for i in out))
