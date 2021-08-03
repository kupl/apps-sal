class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parents = {}

        def find(p):
            if p not in parents:
                parents[p] = p
            if parents[p] != p:
                parents[p] = find(parents[p])
            return parents[p]

        def merge(p, q):
            i, j = find(p), find(q)
            if i != j:
                parents[j] = i

        def isconnected(p, q):
            return find(p) == find(q)

        n = len(points)
        pq = []
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(pq, [dist, i, j])

        edge = 0
        res = 0
        while edge < n - 1:
            dist, i, j = heapq.heappop(pq)
            if isconnected(i, j):
                continue
            else:
                edge += 1
                res += dist
                merge(i, j)
        return res
