def main(n, m, ab):
    g = [set((j for j in range(n) if j != i)) for i in range(n)]
    for (i, (a, b)) in enumerate(ab):
        (a, b) = (a - 1, b - 1)
        g[a].discard(b)
        g[b].discard(a)
    xy = []
    mi = set(range(n))
    seen = [-1] * n
    while mi:
        v = mi.pop()
        todo = [[v, -1]]
        seen[v] = 0
        xyi = [0, 0]
        xyi[0] += 1
        while todo:
            (v, p) = todo.pop()
            for nv in g[v]:
                if nv == p:
                    continue
                if seen[nv] == -1:
                    seen[nv] = (seen[v] + 1) % 2
                    xyi[seen[nv]] += 1
                    mi.discard(nv)
                    todo.append([nv, v])
                elif seen[nv] != (seen[v] + 1) % 2:
                    return -1
        xy.append(xyi)
    abl = [0] * (n + 1)
    abl[0] = 1
    for (x, y) in xy:
        for i in range(n, -1, -1):
            if abl[i] > 0:
                abl[i] = 0
                abl[i + x] = 1
                abl[i + y] = 1
    ans = m
    for (i, x) in enumerate(abl):
        if x == 0:
            continue
        j = n - i
        ans = min(ans, i * (i - 1) // 2 + j * (j - 1) // 2)
    return ans


(n, m) = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
print(main(n, m, ab))
