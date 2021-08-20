from queue import PriorityQueue
from collections import defaultdict


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = defaultdict(int)
        weight = defaultdict(int)

        def make_set(x: int):
            if x in parent:
                return
            parent[x] = x
            weight[x] = 1

        def find(x: int) -> int:
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]

        def union_set(x: int, y: int):
            (px, py) = (find(x), find(y))
            if px == py:
                return
            if weight[px] > weight[py]:
                parent[py] = px
                weight[px] += weight[py]
            else:
                parent[px] = py
                weight[py] += weight[px]
        n = len(points)
        ls = []
        for i in range(n):
            for j in range(i + 1, n):
                (x1, y1) = points[i]
                (x2, y2) = points[j]
                ls.append([abs(x1 - x2) + abs(y1 - y2), i, j])
        ls.sort()
        cost = 0
        for (c, x, y) in ls:
            make_set(x)
            make_set(y)
            if find(x) == find(y):
                continue
            union_set(x, y)
            cost += c
        return cost
