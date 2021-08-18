from math import hypot
import sys
read = sys.stdin.read
readline = sys.stdin.readline

xs, ys, xt, yt = list(map(int, readline().split()))
n, = list(map(int, readline().split()))

xyr = [tuple(map(int, readline().split())) for _ in range(n)] + [(xs, ys, 0), (xt, yt, 0)]


"""
d: 隣接行列に対する Dijkstra
O(N^2)
"""


def Dijkstra_matrix(d, start):
    n = len(d)
    INF = float("inf")
    dist = d[start][:]

    used = [0] * n
    used[start] = 1
    for _ in range(n - 1):
        d0 = INF
        idx = -1
        for i in range(n):
            if not used[i] and dist[i] < d0:
                idx = i
                d0 = dist[i]
        if idx == -1:
            return dist
        else:
            used[idx] = 1
            for j in range(n):
                if not used[j] and dist[j] > dist[idx] + d[idx][j]:
                    dist[j] = dist[idx] + d[idx][j]
    return dist


d = [[max(0.0, hypot((xi - xj), (yi - yj)) - ri - rj) for xj, yj, rj in xyr] for xi, yi, ri in xyr]

dist = Dijkstra_matrix(d, n)
print((dist[-1]))
