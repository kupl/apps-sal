import math

from scipy.special import comb


def Bornoulli(i):
    if i == 0:
        return 1
    elif i == 1:
        return -0.5
    elif i % 2 == 1:
        return 0
    else:
        s = 0
        for k in range(i):
            s -= comb(i, k) * Bornoulli(k) / (i - k + 1)
        return s


def series(k, nb):
    if k >= 2:
        if k % 2 == 1:
            return sum(1 / i**k for i in range(1, nb + 1))
        else:
            return 0.5 * abs(Bornoulli(k)) * (2 * math.pi) ** k / math.factorial(k)
    elif k < -1:
        return (-1) ** k * Bornoulli(-k + 1) / (-k + 1)
