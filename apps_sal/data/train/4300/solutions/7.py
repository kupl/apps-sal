from itertools import combinations as c


def solve(a, b):
    tot = 0
    a = tuple(a)
    b = [i for i in b if i in a]
    for k in range(len(b)):
        if b[k] != a[0]:
            continue
        for kk in range(k + 1, len(b)):
            if b[kk] != a[1]:
                continue
            for i in c(b[kk + 1:], len(a) - 2):
                if i == a[2:]:
                    tot += 1
    return tot
