from collections import defaultdict


def isomorph(a, b):
    print(a, b)
    da, db = defaultdict(list), defaultdict(list)
    for i in range(len(a) == len(b) and len(a)):
        if da[a[i]] != db[b[i]]:
            return False
        da[a[i]].append(i)
        db[b[i]].append(i)
    return bool(da)
