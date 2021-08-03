import math


def sum_of_threes(n):
    res = []
    for i in range(round(math.log(n, 3)), -1, -1):
        if 3**i <= n:
            res.append(i)
            n -= 3**i
            if n == 0:
                return '+'.join('3^{}'.format(i) for i in res)
    return 'Impossible'
