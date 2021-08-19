from heapq import heapify, heappop, heappush
from math import hypot
import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def dijkstra(G, s=0):  # sを始点とした最短経を求める
    n = len(G)
    dist = [INF] * n
    dist[s] = 0
    q = [(0, s)]
    while q:
        d, v = heappop(q)
        if dist[v] < d:
            continue
        for e, cost in G[v]:
            if dist[e] > dist[v] + cost:
                dist[e] = dist[v] + cost
                heappush(q, (dist[e], e))
    return dist


def main():
    sy, sx, gy, gx = map(int, input().split())
    N = int(input())
    circles = [(sy, sx, 0)] + [tuple(map(int, input().split())) for _ in range(N)] + [(gy, gx, 0)]
    N += 2

    G = [[] for _ in range(N)]
    for i in range(N):
        x, y, z = circles[i]
        for j in range(i + 1, N):
            p, q, r = circles[j]
            d = max(0, hypot(x - p, y - q) - z - r)
            G[i].append((j, d))
            G[j].append((i, d))

    dist = dijkstra(G)
    ans = dist[-1]
    print(ans)


def __starting_point():
    main()


__starting_point()
