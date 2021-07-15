from heapq import nlargest

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        visited = [False] * n
        dist = [float(\"inf\")] * n
        curr = 0
        for i in range(n-1):
            x1,y1 = points[curr]
            visited[curr] = True
            for j in range(n):
                if not visited[j]:
                    x2,y2 = points[j]
                    dist[j] = min(dist[j], abs(x2-x1) + abs(y2-y1))
                    
            cost, curr = float(\"inf\"), -1
            for i in range(len(dist)):
                if dist[i] < cost:
                    curr = i
                    cost = dist[i]
            dist[curr] = float(\"inf\")
            res += cost
            
        return res
                    
        
            
