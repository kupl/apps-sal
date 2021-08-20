def main():
    (n, m) = list(map(int, input().split()))
    l = [[] for _ in range(n + 1)]
    for _ in range(m):
        (u, v) = list(map(int, input().split()))
        l[u].append(v)
        l[v].append(u)
    res = [0] * (n + 1)
    for (u, x) in enumerate(res):
        if not x:
            (x, nxt) = (-1, [u])
            while nxt:
                (x, cur, nxt) = (-x, nxt, [])
                for u in cur:
                    if l[u]:
                        res[u] = x
                        for v in l[u]:
                            if not res[v]:
                                nxt.append(v)
                            elif res[v] == x:
                                print(-1)
                                return
    for x in (-1, 1):
        l = [u for u in range(1, n + 1) if res[u] == x]
        print(len(l))
        print(' '.join(map(str, l)))


def __starting_point():
    main()


__starting_point()
