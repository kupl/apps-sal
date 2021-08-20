(dt, a) = (None, None)


def dfs(z):
    r = [{}, {}]
    ln = len(dt[z])
    if ln == 0:
        r[0][0] = 0
        r[1][1 << a[z]] = 1
    elif ln == 1:
        l = dfs(dt[z][0])
        r[0] = l[1]
        for m in l[0]:
            r[1][1 << a[z] | m] = min(r[1][1 << a[z] | m], l[0][m] + 1) if 1 << a[z] | m in r[1] else l[0][m] + 1
        for m in l[1]:
            r[1][1 << a[z] | m] = min(r[1][1 << a[z] | m], l[1][m] + 1) if 1 << a[z] | m in r[1] else l[1][m] + 1
    elif ln == 2:
        l0 = dfs(dt[z][0])
        l1 = dfs(dt[z][1])
        for i0 in range(2):
            for i1 in range(2):
                for m0 in l0[i0]:
                    for m1 in l1[i1]:
                        r[1][1 << a[z] | m0 | m1] = min(r[1][1 << a[z] | m0 | m1], l0[i0][m0] + l1[i1][m1] + 1) if 1 << a[z] | m0 | m1 in r[1] else l0[i0][m0] + l1[i1][m1] + 1
        for m0 in l0[1]:
            for m1 in l1[1]:
                r[0][m0 | m1] = min(r[0][m0 | m1], l0[1][m0] + l1[1][m1]) if m0 | m1 in r[0] else l0[1][m0] + l1[1][m1]
    return r


t = int(input())
for i in range(t):
    (n, m, k) = map(int, input().split())
    a = [0] + [int(x) - 1 for x in input().split()]
    dt = [[] for i in range(n + 1)]
    for i in range(m):
        (u, v) = map(int, input().split())
        dt[u].append(v)
    r = dfs(1)
    k = (1 << k) - 1
    if k in r[0]:
        v = min(r[0][k], r[1][k])
    elif k in r[1]:
        v = r[1][k]
    else:
        v = -1
    print(v)
