def main():
    n = int(input())
    l = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = list(map(int, input().split()))
        l[u].append(v)
        l[v].append(u)
    sw = [a != b for a, b in zip(input()[::2], input()[::2])]
    root = (1, False, False)
    nxt, res, avail = [root], [0], [True] * (n + 1)
    while nxt:
        cur, nxt = nxt, []
        for v, a, b in cur:
            if sw[v - 1] != a:
                a = not a
                res.append(v)
            avail[v] = False
            for u in l[v]:
                if avail[u]:
                    nxt.append((u, b, a))
    res[0] = len(res) - 1
    print('\n'.join(map(str, res)))


def __starting_point():
    main()


__starting_point()
