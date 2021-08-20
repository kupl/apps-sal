from functools import reduce


def nCr(n, k):
    numer = reduce(lambda x, y: x * y, list(range(n, n - k, -1)))
    denom = reduce(lambda x, y: x * y, list(range(1, k + 1)))
    return numer // denom


def bouncy_count(number):
    r = int(nCr(number + 10, 10) + nCr(number + 9, 9) - 2 - 10 * number)
    return 10 ** number - r % (1000000000000000000 + 7) - 1
