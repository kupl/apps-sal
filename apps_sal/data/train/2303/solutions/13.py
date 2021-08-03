def main():
    from heapq import heappush, heappop, heapify
    inf = 2**31 - 1
    n, m, *t = map(int, open(0).read().split())
    z = []
    for a, b, c in zip(t[::3], t[1::3], t[2::3]):
        z.extend([a, b, a + n * c, b + n * c])
    z = {i: v for v, i in enumerate(sorted(set(z)))}
    try:
        z[1]
    except:
        print(-1)
        return
    edge = [[]for _ in range(len(z))]
    d = {}
    l = []
    for a, b, c in zip(t[::3], t[1::3], t[2::3]):
        if b < a:
            a, b = b, a
        i, j, x, y = z[a], z[b], z[a + n * c], z[b + n * c]
        if b == n:
            l.append(y)
        edge[i].append((1, x))
        edge[j].append((1, y))
        edge[x].extend([(0, i), (0, y)])
        edge[y].extend([(0, j), (0, x)])
    used = [False] + [True] * ~-len(z)
    d = [0] + [inf] * ~-len(z)
    edgelist = edge[0]
    heapify(edgelist)
    while edgelist:
        m = heappop(edgelist)
        if not used[m[1]]:
            continue
        d[m[1]] = m[0]
        used[m[1]] = False
        for e in edge[m[1]]:
            if used[e[1]]:
                heappush(edgelist, (e[0] + m[0], e[1]))
    a = min([d[i]for i in l] or [inf])
    print([a, -1][a == inf])


def __starting_point():
    main()


__starting_point()
