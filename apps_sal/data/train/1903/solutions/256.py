class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        connected = 1
        visited = set()
        pq = list()
        i = 0
        while (connected < n):
            visited.add(i)
            for j in range(n):
                if j not in visited:
                    heappush(pq, (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), j))
            d, i = heappop(pq)
            while (i in visited):
                d, i = heappop(pq)
            res += d
            connected += 1
        return res
