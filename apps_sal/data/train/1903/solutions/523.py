class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(a):
            if a != root[a]:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            a, b = find(a), find(b)
            if a == b:
                return 0
            root[a] = b
            return 1
        root = [i for i in range(len(points))]
        res = 0
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                a, b = points[i]
                c, d = points[j]
                edges.append([abs(a - c) + abs(b - d), i, j])
        edges.sort()
        us = 0
        while us != len(points) - 1:
            dis, i, j = edges.pop(0)
            if union(i, j):
                res += dis
                us += 1
        return res
