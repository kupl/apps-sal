from math import factorial as f
import numpy as np


def combination(n, k):
    return f(n) // (f(k) * f(n - k))


def bern(target_level):
    b0 = 1
    b1 = -(1. / 2.)
    bern_nums = [b0, b1]
    n = 3
    while n <= target_level + 1:
        ser = []
        k = 0
        comb_list = []
        while k < n - 1:
            comb_list.append(combination(n, k))
            k += 1
        result_l = [c * b for c, b in zip(comb_list, bern_nums)]
        result_s = 0
        for element in result_l:
            result_s += element
        b_k = -result_s / combination(n, k)
        bern_nums.append(b_k)
        n += 1
    return bern_nums[-1]


def series(k, nb):
    if k > 2 and k % 2 != 0:
        n = 1
        result = 0
        while n <= nb:
            result += 1 / (n**k)
            n += 1
        return result
    elif k >= 2 and k % 2 == 0:
        bern_num = bern(k)
        return 1. / 2. * abs(bern_num) * (2 * np.pi)**k / f(k)
    else:
        k = abs(k)
        bern_num = bern(k + 1)
        return (-1)**k * bern_num / (k + 1)
    return 0
