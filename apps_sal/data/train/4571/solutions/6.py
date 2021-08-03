from math import log


def decompose(num):
    k, ks = 2, []
    while num:
        p = int(log(num, k))
        if p < 2:
            break
        ks.append(p)
        num, k = num - k**p, k + 1
    return [ks, num]
