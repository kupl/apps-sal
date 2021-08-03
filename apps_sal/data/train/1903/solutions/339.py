class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        def distance(point1, points):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points[i + 1:]):
                edges.append((i, j + i + 1, distance(point1, point2)))

        edges = sorted(edges, key=lambda x: -x[2])

        union = list(range(n))
        rank = [1] * n

        def find(x):
            if union[x] != x:
                union[x] = find(union[x])
            return union[x]

        def connect(x, y):
            xr, yr = find(x), find(y)
            if rank[xr] > rank[yr]:
                union[yr] = xr
                rank[xr] += rank[yr]
            else:
                union[xr] = yr
                rank[yr] += rank[xr]

        result = 0
        times = 0
        while(edges and times < n - 1):
            p1, p2, dis = edges.pop()
            if find(p1) != find(p2):
                connect(p1, p2)
                result += dis
                times += 1
        print(rank)
        return result
