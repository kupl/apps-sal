import queue as q


def ds(x):
    ss = 0
    x = str(x)
    l = len(x)
    for i in range(l):
        m = int(x[i])
        ss += m
    return int(ss)


t = int(input())
while t:
    t = t - 1
    (n, d) = map(int, input().split())
    a = {n: 0}
    i = 0
    arr = q.Queue(maxsize=100000000000000)
    arr.put((n, 0))
    while i < 100000:
        x = arr.get()
        p1 = ds(x[0])
        p2 = x[0] + d
        if p1 < 10 and (not p1 in a):
            a[p1] = x[1] + 1
        if p2 < 10 and (not p2 in a):
            a[p2] = x[1] + 1
        arr.put((p1, x[1] + 1))
        arr.put((p2, x[1] + 1))
        i += 1
    nn = min(a)
    print(nn, a[nn])
