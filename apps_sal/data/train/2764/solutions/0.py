from bisect import bisect_right as bisect
RES = [[] for _ in range(11)]
for c in range(1, 1001):
    c3 = c ** 3
    nSol = sum((((c3 - a ** 2) ** 0.5).is_integer() for a in range(1, int((c3 // 2) ** 0.5 + 1))))
    if 0 < nSol < 11:
        RES[nSol].append(c)


def find_abc_sumsqcube(c_max, nSol):
    return RES[nSol][:bisect(RES[nSol], c_max)]
