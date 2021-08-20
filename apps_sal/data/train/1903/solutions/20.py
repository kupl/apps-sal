class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dsu = DSU()
        min_heap = []
        for i in range(len(points)):
            (x1, y1) = (points[i][0], points[i][1])
            for j in range(i + 1, len(points)):
                (x2, y2) = (points[j][0], points[j][1])
                heappush(min_heap, (abs(x1 - x2) + abs(y1 - y2), (x1, y1, x2, y2)))
        cost = 0
        while min_heap:
            (c, (x1, y1, x2, y2)) = heappop(min_heap)
            if dsu.find((x1, y1)) != dsu.find((x2, y2)):
                cost += c
                dsu.union((x1, y1), (x2, y2))
        return cost


class DSU:

    def __init__(self):
        self.father = {}

    def find(self, a):
        self.father.setdefault(a, a)
        if a != self.father[a]:
            self.father[a] = self.find(self.father[a])
        return self.father[a]

    def union(self, a, b):
        _a = self.find(a)
        _b = self.find(b)
        if _a != _b:
            self.father[_a] = _b
