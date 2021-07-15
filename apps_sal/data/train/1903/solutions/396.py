from heapq import *

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        if len(points) == 1:
            return result
        
        costHeap = []
        n = len(points)
        cur = 0
        distance = lambda p, np: abs(p[0] - np[0]) + abs(p[1] - np[1])
        visited = set()
        visited.add(cur)
        
        for i in range(1, n):
            heappush(costHeap, [distance(points[0], points[i]), i])
        
        while costHeap:
            cost, nextStart = heappop(costHeap)
            # print(cur, nextStart, cost)
            if nextStart not in visited:
                result += cost
                visited.add(nextStart)
                cur = nextStart
                for i in range(n):
                    if i in visited:
                        continue
                    heappush(costHeap, [distance(points[cur], points[i]), i])
            if len(visited) == n:
                break
                
        return result
                    

