import math


def sum_of_threes(n):
    p = []
    while n:
        x, y = math.log(n, 3), n % 3
        x = int(x + 1 * (abs(x % 1 - 1) < 1e-8))
        if y > 1 or p and x == p[-1]:
            return "Impossible"
        p.append(x)
        n = n - 3**x

    return '+'.join("3^{}".format(x) for x in sorted(p, reverse=True))
