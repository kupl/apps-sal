from heapq import *
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        points = [tuple(point) for point in points]
        currPoint = points[0]
        vis = set()
        que = [[0, currPoint]]
        
        def getDist(a, b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        ans = 0
        while que:
            dist, cpoint = heappop(que);
            if cpoint in vis:
                continue
            ans+=dist
            vis.add(cpoint)
            for point in points:
                if point not in vis:
                    newDist = getDist(cpoint, point)
                    heappush(que, [newDist, point])
        return ans
            
            

