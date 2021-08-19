from itertools import accumulate, count
from collections import defaultdict
from operator import mul


def gen():
    D = defaultdict(list)
    for q in count(2):
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D[p + q].append(p)
            del D[q]


(create, save) = (accumulate(gen(), mul), [1])


def num_primorial(n):
    while len(save) <= n:
        save.append(next(create))
    return save[n]
