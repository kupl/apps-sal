t = int(input())
for test in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    m = -1
    rv = -1
    t = -1
    for x in range(n):
        if t < l[x] * r[x]:
            m = x + 1
            t = l[x] * r[x]
            rv = r[x]
        elif t == l[x] * r[x]:
            if rv < r[x]:
                m = x + 1
                t = l[x] * r[x]
                rv = r[x]
    print(m)
