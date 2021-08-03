class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        if n <= 1:
            return 0

        edges = []
        for i, coor in enumerate(points):
            x1, y1 = coor
            for j in range(i + 1, n):
                x2, y2 = points[j]
                edges.append((abs(x1 - x2) + abs(y1 - y2), i, j))

        root = [i for i in range(n)]

        def union(p, q):
            r1, r2 = find(p), find(q)
            if r1 != r2:
                root[r1] = r2
                return False
            return True

        def find(p):
            if p == root[p]:
                return p

            root[p] = find(root[p])
            return root[p]

        distance = 0
        for d, p1, p2 in sorted(edges):
            if not union(p1, p2):
                distance += d

        return distance
