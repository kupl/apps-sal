class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        heap = []
        f = [d for d in range(len(points))]

        def find(x):
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)
        res = 0
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))
        while heap:
            (val, i, j) = heapq.heappop(heap)
            if find(i) != find(j):
                union(i, j)
                res += val
        return res
