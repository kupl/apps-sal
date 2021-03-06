def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    (n, m) = map(int, input().split())
    g = tuple((list() for _ in range(n)))
    for _ in range(m):
        (u, v, c) = (int(x) - 1 for x in input().split())
        c += 1
        g[u].append((v, c))
        g[v].append((u, c))

    def make_label(r):
        ret = [-1] * n
        ret[r] = 1
        vis = [False] * n
        vis[r] = True
        dq = deque()
        dq.append(r)
        while dq:
            v = dq.popleft()
            for (u, c) in g[v]:
                if vis[u]:
                    continue
                vis[u] = True
                if ret[v] == c:
                    if c == n:
                        ret[u] = 1
                    else:
                        ret[u] = c + 1
                else:
                    ret[u] = c
                dq.append(u)
        return ret
    lbl = make_label(0)
    print(*lbl, sep='\n')


def __starting_point():
    main()


__starting_point()
