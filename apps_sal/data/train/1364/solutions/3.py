from collections import defaultdict

for x in range(int(input())):
    n, r = list(map(int, input().split()))
    d = defaultdict(list)
    p = defaultdict(list)
    for i in range(n):
        a, b = list(map(int, input().split()))
        if b - a < 0:
            d[a - b].append(a)
        else:
            p[b - a].append(a)

    if r > 0:
        k = 0
        s = 0
        for e in d:
            c = defaultdict(list)
            for f in d[e]:
                c[f % r].append(f)
            for i in c:
                L = c[i]
                L.sort()
                w = len(c[i])
                h = w // 2
                for t in range(w):
                    s += abs(L[t] - L[h]) // r

                k += 1
        for e in p:
            c = defaultdict(list)
            for f in p[e]:
                c[f % r].append(f)
            for i in c:
                L = c[i]
                L.sort()
                w = len(c[i])
                h = w // 2
                for t in range(w):
                    s += abs(L[t] - L[h]) // r

                k += 1
        print(k, s)
    else:
        k = 0
        s = 0
        for e in d:

            k += len(d[e])
        for e in p:

            k += len(p[e])
        print(k, s)
