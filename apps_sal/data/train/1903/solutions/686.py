from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        n = len(points)
        c = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                dist = manhattan(points[i], points[j])
                c[i].append((dist, j))
                c[j].append((dist, i))
        
        pq = c[0]
        heapq.heapify(pq)
        visited = [False] * n
        visited[0] = True
        cnt = 1
        res = 0
        while pq:
            d, j = heapq.heappop(pq)
            if not visited[j]:
                cnt += 1
                res += d
                visited[j] = True
                for record in c[j]:
                    heapq.heappush(pq, record)
                if cnt >= n:
                    break
                    
        return res
                
            
                
        
        


