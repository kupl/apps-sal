import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x, y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        res, n = 0, len(points)
        seen = set()
        vertices = [(0, (0, 0))]
        
        while len(seen) < n:
            d, (u, v) = heapq.heappop(vertices)            
            if u in seen and v in seen: continue
            res += d
            seen.add(v)
            for j in range(n):
                if j not in seen and j != v:
                    heapq.heappush(vertices, (manhattan(points[j], points[v]), (v, j)))
                    
        return res
