class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parents = [i for i in range(n)]
        groups = n

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        distance = 0
        heap = []
        for i in range(n):
            for j in range(i):
                heapq.heappush(heap, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j))

        while heap or groups > 1:
            dist, i, j = heapq.heappop(heap)
            ri, rj = find(i), find(j)
            if ri != rj:
                groups -= 1
                parents[ri] = rj
                distance += dist
        return distance
