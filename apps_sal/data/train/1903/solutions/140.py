from collections import defaultdict
import heapq


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        (heap, c, ans) = (list(), 0, 0)
        parent = [-1] * len(points)
        if len(points) == 1 or not points:
            return 0

        def give_dist(x, y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heap.append([give_dist(points[i], points[j]), i, j])
        heapq.heapify(heap)

        def find(x):
            if parent[x] == -1:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            (px, py) = (find(x), find(y))
            parent[px] = py
        while c < len(points) - 1:
            (d, x, y) = heapq.heappop(heap)
            if find(x) != find(y):
                ans += d
                union(x, y)
                c += 1
        return ans
