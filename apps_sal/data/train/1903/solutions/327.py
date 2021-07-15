class Solution:
    
    def dist(self, x1,y1,x2,y2):
        return abs(x1-x2) + abs(y1-y2)
    
    def dist_from_point_to_all(self, points, i, n):
        return [self.dist(*points[i],*points[j]) for j in range(n)]
        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        # This is Prim algo and I need an array for the min_priority
        # to get the algo in time O(n**2), otherwise it will be too
        # slow with a factor of log(n)
        all_ = set(range(n))
        s = set([0])
        tot = 0
        dist = self.dist_from_point_to_all(points, 0, n)
        for _ in range(n-1):
            min_dist = 10**8
            for i in range(n):
                if i not in s and dist[i] < min_dist:
                    pos_best = i
                    min_dist = dist[i]
            tot += min_dist
            s.add(pos_best)
            dist_pos_best = self.dist_from_point_to_all(points, pos_best, n)
            dist = [min(dist[j], dist_pos_best[j]) for j in range(n)]
        return tot
