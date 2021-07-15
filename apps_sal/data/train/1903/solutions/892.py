class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def hash_point(point):
            return point[0],point[1]
        
        def manh_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        
        if len(points) == 1: return 0
        if len(points) == 2: return manh_dist(points[0], points[1])
        
        points_remaining = set()
        dists = []
        first_point = points[0]
        
        for i in range(1, len(points)):
            point,h_point = points[i],hash_point(points[i])
            points_remaining.add(h_point)
            heapq.heappush(dists, (manh_dist(first_point, point), h_point))
        
        ans = 0
        
        while points_remaining and dists:
            dist,point = heapq.heappop(dists)
            
            if point not in points_remaining: continue
                
            points_remaining.remove(point)
            ans += dist
            
            for p in points_remaining:
                heapq.heappush(dists, (manh_dist(point, p), p))
                
        return ans

