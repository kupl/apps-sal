def main():
    from math import hypot
    import sys
    input = sys.stdin.readline
    inf = 1 << 60
    (xs, ys, xt, yt) = list(map(int, input().split()))
    N = int(input())

    def dist(p1, p2):
        d = hypot(p1[0] - p2[0], p1[1] - p2[1])
        return max(0, d - (p1[2] + p2[2]))
    ps = [(xs, ys, 0)]
    ps += (tuple(map(int, input().split())) for _ in range(N))
    ps += [(xt, yt, 0)]
    adj = [[inf] * (N + 2) for _ in range(N + 2)]
    for (i, p1) in enumerate(ps):
        for (j, p2) in enumerate(ps):
            if i <= j:
                break
            adj[i][j] = adj[j][i] = dist(p1, p2)

    def dijkstra(s):
        dist = [inf] * (N + 2)
        dist[s] = 0
        det = [0] * (N + 2)
        (c, v) = (0, s)
        det[s] = 1
        for _ in range(N + 1):
            for (u, dc) in enumerate(adj[v]):
                nc = c + dc
                if dist[u] <= nc:
                    continue
                dist[u] = nc
            (c, v) = (-1, -1)
            for (u, d) in enumerate(dist):
                if det[u]:
                    continue
                if ~v and c <= d:
                    continue
                (c, v) = (d, u)
            det[v] = 1
        return dist
    print(dijkstra(s=0)[N + 1])


def __starting_point():
    main()


__starting_point()
