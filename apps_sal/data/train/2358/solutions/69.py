def main():
    from math import hypot
    import sys
    input = sys.stdin.readline

    inf = 1 << 60

    xs, ys, xt, yt = list(map(int, input().split()))
    N = int(input())
    N += 2

    def dist(p1, p2):
        d = hypot(p1[0] - p2[0], p1[1] - p2[1])
        return max(0, d - (p1[2] + p2[2]))

    s = (xs, ys, 0, 0)
    g = (xt, yt, 0, N - 1)
    ps = [s, g]
    adj = [[inf] * N for _ in range(N)]
    adj[0][N - 1] = adj[N - 1][0] = dist(s, g)
    for idx1 in range(1, N - 1):
        *p1, = list(map(int, input().split()))
        p1.append(idx1)
        for *p2, idx2 in ps:
            d = dist(p1, p2)
            adj[idx1][idx2] = adj[idx2][idx1] = d
        ps.append(p1)

    def dijkstra(s):
        from heapq import heappop, heappush

        dist = [inf] * N

        h = [(0, s)]
        dist[s] = 0

        while h:
            c, v = heappop(h)
            if dist[v] < c:
                continue

            for u, dc in enumerate(adj[v]):
                nc = c + dc
                if dist[u] <= nc:
                    continue
                dist[u] = nc
                heappush(h, (nc, u))

        return dist

    print((dijkstra(s=0)[N - 1]))


def __starting_point():
    main()


__starting_point()
