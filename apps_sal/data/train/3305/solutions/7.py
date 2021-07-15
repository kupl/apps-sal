def shortest(N, es):
    ee = [[] for _ in range(N)]
    for f, t, w in es:
        ee[f].append((t, w))
    dd = [0x7f7f7f7f for _ in range(N)]
    f = [False for _ in range(N)]
    dd[0] = 0
    q = [0]
    f[0] = True
    while len(q) > 0:
        k = q.pop()
        f[k] = False
        for t, w in ee[k]:
            if dd[t] > dd[k] + w:
                dd[t] = dd[k] + w
                if not f[t]:
                    q.append(t)
                    f[t] = True
    return -1 if dd[N - 1] == 0x7f7f7f7f else dd[N - 1]
