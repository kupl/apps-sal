def search(l, n, k):
    r = []
    o = []
    p = []
    t = []
    e = []
    for i in range(k):
        o.append(-1)
    for i in range(n):
        r.append(i)
        for j in range(1, k + 1, 1):
            if(l[i] == j):
                o.append(i)
            else:
                o.append(o[len(o) - k])

    for i in range(k, len(o), k):
        for j in range(k):
            p.append(o[i + j])
        q = min(p)
        t.append(q)
        p.clear()

    for i in range(len(r)):
        y = r[i] - t[i]
        e.append(y)

    print(max(e))


t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    l = list(map(int, input().split()))
    search(l, n, k)
