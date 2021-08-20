class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        def dist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        heap = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                heap.append((dist(i, j), i, j))
        heapq.heapify(heap)

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        def union(i, j):
            p[find(i)] = find(j)
        p = list(range(n))
        num_edges = 0
        res = 0
        while heap and num_edges < n:
            (d, i, j) = heapq.heappop(heap)
            if find(i) == find(j):
                continue
            union(i, j)
            num_edges += 1
            res += d
        return res
