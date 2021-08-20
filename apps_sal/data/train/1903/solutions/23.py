class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0
        distances = []
        for i in range(n):
            for j in range(i + 1, n):
                (xi, yi) = points[i]
                (xj, yj) = points[j]
                heapq.heappush(distances, (abs(xi - xj) + abs(yi - yj), i, j))
        uf = {}

        def find(i: int) -> int:
            if i not in uf:
                uf[i] = i
            while uf[i] != uf[uf[i]]:
                uf[i] = find(uf[i])
            return uf[i]

        def union(i: int, j: int) -> None:
            uf[find(i)] = find(j)
        dist = 0
        while distances:
            (d, i, j) = heapq.heappop(distances)
            if find(i) != find(j):
                union(i, j)
                dist += d
        return dist
