class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        parents = list(range(n))

        def find(i):
            if parents[i] != i:
                parents[i] = find(parents[i])
            return parents[i]

        def union(i, j):
            p_i = find(i)
            p_j = find(j)
            if p_i != p_j:
                if p_i > p_j:
                    parents[p_j] = p_i
                else:
                    parents[p_i] = p_j
        heap = []
        for i in range(n):
            for j in range(i + 1, n):
                heapq.heappush(heap, (self.distance(points[i], points[j]), i, j))
        res = 0
        while heap:
            (dist, i, j) = heapq.heappop(heap)
            if find(i) == find(j):
                continue
            union(i, j)
            res += dist
        return res

    def distance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
