import itertools
import numpy as np


def sum_1(n):
    ketas = list(map(int, str(n)))
    pattern = [itertools.combinations(ketas, i + 1) for i in range(len(ketas))]
    pattern = list(itertools.chain.from_iterable(pattern))
    pattern = [''.join(map(str, i)) for i in pattern]
    sum = np.sum([int(i) for i in pattern])
    return sum


def sum_2(n):
    ketas = list(map(int, str(n)))
    i_s = itertools.combinations(list(range(len(ketas) + 1)), 2)
    pattern_i = [ketas[i:j] for i, j in i_s]
    sum = np.sum([int(''.join(map(str, i))) for i in pattern_i])
    return sum


def common_divisors(a, b):
    while b:
        a, b = b, a % b
    d = 1
    while a % 2 == 0:
        d += 1
        a /= 2
    e = 3
    while a > 1:
        c = 1
        while a % e == 0:
            c += 1
            a /= e
        d *= c
        e += 2
    return d - 1


def find_int_inrange(a, b):
    # your code here
    maxlen = 0
    result = []
    for i in range(a, b):
        divisors = common_divisors(sum_1(i), sum_2(i))
        if divisors > maxlen:
            maxlen = divisors
            result = [maxlen, i]
        elif divisors == maxlen:
            result.append(i)
    return result
