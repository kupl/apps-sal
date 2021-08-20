def main():
    from collections import deque
    import sys
    input = sys.stdin.readline
    (n, m) = map(int, input().split())
    g = tuple((list() for _ in range(n)))
    for _ in range(m):
        (u, v, c) = (int(x) - 1 for x in input().split())
        g[u].append((v, c))
        g[v].append((u, c))

    def make_tree(r, g):
        ret = tuple((list() for _ in range(n)))
        dq = deque()
        dq.append(r)
        vis = [False] * n
        vis[r] = True
        while dq:
            v = dq.popleft()
            for (u, c) in g[v]:
                if vis[u]:
                    continue
                vis[u] = True
                ret[v].append((u, c))
                dq.append(u)
        return ret
    gt = make_tree(0, g)

    def make_label(r, g):
        ret = [-1] * n
        ret[r] = 0
        dq = deque()
        dq.append(r)
        while dq:
            v = dq.popleft()
            for (u, c) in g[v]:
                if ret[v] == c:
                    ret[u] = (c + 1) % n
                else:
                    ret[u] = c
                dq.append(u)
        return ret
    label = make_label(0, gt)
    ans = map(lambda e: e + 1, label)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
