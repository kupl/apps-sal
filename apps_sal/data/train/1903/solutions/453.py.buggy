import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_of_points = len(points)
        if num_of_points == 1:
            return 0
        distance = [[float(\"inf\") for _ in range(num_of_points)] for _ in range(num_of_points)]
        for i in range(num_of_points):
            for j in range(i+1, num_of_points):
                temp_distance = self.countDistance(points[i], points[j])
                distance[i][j] = temp_distance
                distance[j][i] = temp_distance
        visited = [False for _ in range(num_of_points)]
        q = [(0, 0)]
        cost = 0
        heapq.heapify(q)
        while False in visited:
            # print(visited)
            d, node= heapq.heappop(q)
            while visited[node]:
                d, node = heapq.heappop(q)
            visited[node] = True
            cost += d
            for i in range(num_of_points):
                if not visited[i]:
                    heapq.heappush(q, (distance[node][i], i))
        return cost
            
    
            
    def countDistance(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
