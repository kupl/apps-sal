from math import factorial, trunc


def going(n):
    (sum, past) = (1, 1)
    for k in range(n, 1, -1):
        past *= 1 / k
        sum += past
    return trunc(sum * 10 ** 6) / 10 ** 6
