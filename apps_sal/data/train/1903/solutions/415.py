class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
    
        res , n = 0, len(points)
        dist_list = [distance(points[0], p) for p in points]
        for _ in range(n-1):
            d, j = min((d, i) for i, d in enumerate(dist_list) if d > 0)
            res += d
            dist_list = [min(dist_list[i], distance( points[j], p)) for i, p in enumerate(points)]
            
        return res

