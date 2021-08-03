class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        sets = [i for i in range(n + 1)]

        def find(i):
            if i != sets[i]:
                sets[i] = find(sets[i])
            return sets[i]

        def union(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            sets[x] = y
            return 1
        edges = []
        for i in range(n):
            for j in range(i, n):
                edges.append([distance(points[i], points[j]), i, j])

        edges.sort(key=lambda x: x[0])
        weight = 0
        for w, i, j in edges:
            if union(i, j):
                weight += w
        return weight
