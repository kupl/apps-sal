import math
import itertools


def count_find_num(primesL, limit):
    exps = [int(math.log(limit, p)) + 1 for p in primesL]
    exps = exps + [2, 2, 2, 2, 2, 2]
    exps = exps[0:5]
    primesL = (primesL + [1, 1, 1, 1])[0:5]
    res = set()
    for a in range(1, exps[0]):
        for b in range(1, exps[1]):
            for c in range(1, exps[2]):
                for d in range(1, exps[3]):
                    for e in range(1, exps[4]):
                        x = primesL[0] ** a * primesL[1] ** b * primesL[2] ** c * primesL[3] ** d * primesL[4] ** e
                        if x <= limit:
                            res.add(x)
    return [len(res), max(res)] if res else []
