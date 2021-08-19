q = int(input())


def full_way(u):
    res = set()
    while u >= 1:
        res.add(u)
        u //= 2
    return res


def get_way(u, v):
    res1 = full_way(u)
    res2 = full_way(v)
    m = max(res1 & res2)
    res = set()
    for x in res1 | res2:
        if x > m:
            res.add(x)
    return res


d = {}
for i in range(q):
    a = input().split()
    if a[0] == '1':
        (v, u, w) = map(int, a[1:])
        for x in get_way(u, v):
            if x not in d:
                d[x] = 0
            d[x] += w
    else:
        (v, u) = map(int, a[1:])
        res = 0
        for x in get_way(u, v):
            if x in d:
                res += d[x]
        print(res)
