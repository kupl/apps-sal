from itertools import combinations


def find_biggTriang(listPoints):
    s = combinations(listPoints, 3)
    j = 0
    i = 0
    ret = []
    mx = 0
    for (a, b, c) in s:
        s = abs((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2
        if s > mx:
            mx = s
            ret = []
        if s == mx:
            ret.append([list(a), list(b), list(c)])
        if s > 0:
            i += 1
        j += 1
    if len(ret) <= 1:
        ret = ret[0]
    return [len(listPoints), j, i, ret, mx]
