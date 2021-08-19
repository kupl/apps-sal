class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return [self.x, self.y] < [other.x, other.y]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [Point(x, y) for (x, y) in points]
        edges = []

        def getDistance(a, b):
            return abs(a.x - b.x) + abs(a.y - b.y)
        visited = set()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (u, v) = (points[i], points[j])
                edges.append((getDistance(u, v), u, v))
        edges.sort(reverse=True)
        self.parent = {p: p for p in points}
        self.size = {p: 1 for p in points}
        components = len(points)
        total_cost = 0
        while components > 1 and edges:
            (d, u, v) = edges.pop()
            if self.union(u, v):
                total_cost += d
                components -= 1
        return total_cost

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            if self.size[root_a] <= self.size[root_b]:
                self.parent[root_a] = root_b
                self.size[root_b] += self.size[root_a]
            else:
                self.parent[root_b] = root_a
                self.size[root_a] += self.size[root_b]
            return True
        return False

    def find(self, a):
        curr = a
        while self.parent[curr] != curr:
            curr = self.parent[curr]
        (root, curr) = (curr, a)
        while self.parent[curr] != curr:
            (self.parent[curr], curr) = (root, self.parent[curr])
        return root
