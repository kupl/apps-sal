import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        manhattan = lambda p1, p2 : abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        pq = []
        p1 = points[0]
        seen = {0,}
        horizon = set(range(1, len(points)))
        for idx in horizon:
            p2 = points[idx]
            heapq.heappush(pq, (manhattan(p1, p2), idx))

                
        total_dist = 0
        while horizon:
            while pq[0][-1] in seen:
                heapq.heappop(pq)
            dist, min_idx = heapq.heappop(pq)
            
            
            total_dist += dist
            seen.add(min_idx)
            horizon.remove(min_idx)
            
            p1 = points[min_idx]
            
            for idx in horizon: 
                p2 = points[idx]
                heapq.heappush(pq, (manhattan(p1, p2), idx))
                    
        return total_dist
        
        

