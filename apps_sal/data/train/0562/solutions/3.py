n, m = [int(i) for i in input().split()]
sqsets = list(range(2, min(n, m) + 1))
ci = []
for i in range(n):
    ci.append(list(input()))
cc = [[0 for i in range(m + 1)] for j in range(n + 1)]


def cache_creation_part(x, y):
    cc[y][x] = cc[y][x - 1] + cc[y - 1][x] - cc[y - 1][x - 1]
    if (y + x) % 2 == 0:
        cc[y][x] += int(ci[y - 1][x - 1] != '1')
    else:
        cc[y][x] += int(ci[y - 1][x - 1] != '0')


def cache_creation(m, n):
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            cache_creation_part(x, y)


def operation(x, y, k):
    return cc[y + k][x + k] + cc[y][x] - cc[y + k][x] - cc[y][x + k]


c = 0
kd = {k: c for k in sqsets}


def kd_creation(m, n, sqsets):
    cache_creation(m, n)
    for k in sqsets:
        kd[k] = (10**9) + 1
        for y in range(n - k + 1):
            for x in range(m - k + 1):
                cu = operation(x, y, k)
                kd[k] = min(kd[k], cu, k * k - cu)


kd_creation(m, n, sqsets)
del cc
del ci
del sqsets
tc = int(input())
tc = [int(x) for x in input().split()]
for u in tc:
    p = 0
    for i in kd:
        if kd[i] <= u:
            p = max(i, p)
    print(p)
