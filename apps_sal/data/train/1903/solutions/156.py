class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        num_points = len(points)
        mst = {0}
        mra = 0
        hep = []
        def dist(a,b):
            return abs(a[0] - b[0]) + abs(a[1]- b[1])
        
        def update_heap(added):
            for i,(x,y) in enumerate(points):
                if i not in mst:
                    heapq.heappush(hep, (dist(points[added], points[i]), added, i))
        
        sol = 0
        while len(mst) < num_points:
            update_heap(mra)
            
            while hep:
                d, x, y = heapq.heappop(hep)
                
                if y not in mst:
                    mst.add(y)
                    mra = y
                    sol += d
                    break
        
        return sol
                
                
        

