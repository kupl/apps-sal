def main():
    import sys
    input = sys.stdin.readline
    INF = 10 ** 10
    from math import sqrt
    (xs, ys, xg, yg) = map(int, input().split())
    N = int(input())
    XYR = [tuple(map(int, input().split())) for _ in range(N)]
    G = [[] for _ in range(N + 2)]

    def diff1(i, j):
        tmp = (XYR[i][0] - XYR[j][0]) ** 2 + (XYR[i][1] - XYR[j][1]) ** 2
        R = XYR[i][2] + XYR[j][2]
        return max(0, sqrt(tmp) - R)
    for i in range(N - 1):
        for j in range(i + 1, N):
            tmp = diff1(i, j)
            G[i].append((tmp, j))
            G[j].append((tmp, i))

    def diff2(x, y, i):
        tmp = (x - XYR[i][0]) ** 2 + (y - XYR[i][1]) ** 2
        R = XYR[i][2]
        return max(0, sqrt(tmp) - R)
    for i in range(N):
        tmp = diff2(xs, ys, i)
        G[N].append((tmp, i))
        G[i].append((tmp, N))
    for i in range(N):
        tmp = diff2(xg, yg, i)
        G[N + 1].append((tmp, i))
        G[i].append((tmp, N + 1))
    tmp = (xs - xg) ** 2 + (ys - yg) ** 2
    G[N].append((sqrt(tmp), N + 1))
    G[N + 1].append((sqrt(tmp), N))
    d = [INF] * (N + 2)

    def dijksrea(s):
        from heapq import heappop, heappush
        d[s] = 0
        pque = []
        heappush(pque, (0, s))
        while pque:
            p = heappop(pque)
            v = p[1]
            if d[v] < p[0]:
                continue
            for i in range(len(G[v])):
                e = G[v][i]
                if d[e[1]] > d[v] + e[0]:
                    d[e[1]] = d[v] + e[0]
                    heappush(pque, (d[e[1]], e[1]))
    dijksrea(N)
    print(d[N + 1])


def __starting_point():
    main()


__starting_point()
