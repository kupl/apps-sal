import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        res = 0
        n = len(points)
        seen = set()
        h = [(0, 0, 0)]
        
        while len(seen) < n:
            d, u, v = heapq.heappop(h)
            if v in seen: continue
            seen.add(v)
            res += d
            for w in range(n):
                if w in seen or w == v: continue
                heapq.heappush(h, (dist(points[v], points[w]), v, w))
                    
        return res
