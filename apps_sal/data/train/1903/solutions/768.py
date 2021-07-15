class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(u, v):
            x, y = points[u]
            x2, y2 = points[v]
            return abs(x - x2) + abs(y - y2)
        
        n = len(points)
        visited = [False] * (n)
        distto = [0] + [10 ** 7] * (n - 1)
        
        ans = 0
        for _ in range(n):
            best, idx = 10 ** 7, -1
            for u in range(n):
                if not visited[u] and distto[u] < best:
                    best, idx = distto[u], u
            visited[idx] = True
            ans += best
            for v in range(n):
                if not visited[v]:
                    distto[v] = min(distto[v], dist(idx, v))
                
        return ans

