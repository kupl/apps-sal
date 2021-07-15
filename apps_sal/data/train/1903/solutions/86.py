class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = [False] * len(points)
        distance = [[0]*len(points) for p in points]
        queue = [(0,0)] # cost, point_index
        for i in range(len(points)):
            for j in range(len(points)):
                distance[i][j] = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

        res = 0
        while queue:
            cost, point = heapq.heappop(queue)
            if visited[point] == True: continue
            visited[point] = True
            res += cost
            for i in range(len(points)):
                if not visited[i]:
                    heapq.heappush(queue, (distance[point][i], i))
        
        return res           
            

