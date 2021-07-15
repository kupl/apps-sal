class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        distances, n = {i: [] for i in range(len(points))}, len(points)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                distances[i].append((dist, j))
                distances[j].append((dist, i))
        import heapq
        heap = distances[0]
        heapq.heapify(heap)
        ans = 0
        count = 0
        visited = set([0])
        while heap:
            dist, j = heapq.heappop(heap)
            if j not in visited:
                visited.add(j)
                ans += dist
                count += 1
                for x in distances[j]:
                    heapq.heappush(heap, x)
            if count == n -1: break
        return ans
            
    
                
        
        

