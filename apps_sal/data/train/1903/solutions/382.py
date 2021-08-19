from collections import defaultdict
from heapq import heappop, heappush, heapify


def prim(N, E):
    edges = defaultdict(list)
    for (x, y, c) in E:
        edges[x].append((c, y))
        edges[y].append((c, x))
    heap = []
    heappush(heap, (0, 0))
    cnt = 0
    visited = {}
    ans = 0
    while heap:
        (c, n) = heappop(heap)
        if n in visited:
            continue
        visited[n] = 1
        ans += c
        for e in edges[n]:
            heappush(heap, e)
        cnt += 1
        if cnt >= N:
            break
    return ans


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        E = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                E.append((i, j, d))
        ans = prim(n, E)
        return ans
