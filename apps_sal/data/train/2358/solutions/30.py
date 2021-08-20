import heapq
import sys
input = sys.stdin.readline


def dijkstra(n, s, edges):
    hq = [(0, s)]
    cost = [float('inf')] * n
    cost[s] = 0
    while hq:
        (c, v) = heapq.heappop(hq)
        if c > cost[v]:
            continue
        for (d, u) in edges[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost[-1]


def main():
    (xs, ys, xt, yt) = map(int, input().split())
    n = int(input())
    circles = []
    circles.append([xs, ys, 0])
    for _ in range(n):
        circles.append(list(map(int, input().split())))
    circles.append([xt, yt, 0])
    edges = [[] for _ in range(n + 2)]
    for i in range(n + 2):
        for j in range(i + 1, n + 2):
            dx = circles[i][0] - circles[j][0]
            dy = circles[i][1] - circles[j][1]
            d = (dx ** 2 + dy ** 2) ** 0.5
            r = circles[i][2] + circles[j][2]
            edges[i].append([max(0, d - r), j])
            edges[j].append([max(0, d - r), i])
    ans = dijkstra(n + 2, 0, edges)
    print(ans)


main()
