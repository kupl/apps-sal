from itertools import zip_longest


def add(a, b):
    d = ('00', '01', '10', '11')

    arr, k = [], '0'
    for m, n in zip_longest(a[::-1], b[::-1], fillvalue='0'):
        k, r = d[(m, n, k).count('1')]
        arr.append(r)
    arr.append(k)
    return ''.join(arr[::-1]).lstrip('0') or '0'
