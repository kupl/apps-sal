from heapq import heapify, heappush, heappop
from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(point1, point2):
            x1, y1 = point1
            x2, y2 = point2
            return abs(x1-x2) + abs(y1-y2)
        
        n = len(points)
        if n == 1:
            return 0
        
        cost = defaultdict(list)
        for i in range(n):
            point1 = points[i]
            for j in range(i+1, n):
                point2 = points[j]
                d = distance(point1, point2)
                cost[tuple(point1)].append((d, point2))
                cost[tuple(point2)].append((d, point1))
                
                
            
        ans = 0
        visited = {tuple(points[0])}
        heap = cost[tuple(points[0])]
        heapify(heap)
        
        while len(visited) != n:
            d, v = heappop(heap)
            if tuple(v) not in visited:
                visited.add(tuple(v))
                ans += d
                for record in cost[tuple(v)]:
                    heappush(heap, record)
        
        return ans
                    
                    
                
                
        
        
        
        
        
        
            
            
            
                        
                    
            
            
        
        
        

