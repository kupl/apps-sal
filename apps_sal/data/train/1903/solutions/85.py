class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1: return 0
        
        res = 0
        n = len(points)
        visited = set([0])
        cur = 0
        dist = [float('inf')] * n
        
        for _ in range(n-1):
            x, y = points[cur]
            for j, (u, v) in enumerate(points):
                if j in visited: continue
                dist[j] = min(dist[j], abs(x - u) + abs(y - v))

            d, cur = min([(d, j) for j, d in enumerate(dist)])
            dist[cur] = float('inf')
            res += d
            visited.add(cur)

        return res
