import heapq
from collections import defaultdict

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def manhattan(x,y):
            return abs(x[0] - y[0]) + abs(x[1] - y[1])
        
        dist_dict = defaultdict(list)
        n_points = len(points)
        
        for i in range(n_points):
            for j in range(i+1, n_points):
                dist_curr = manhattan(points[i], points[j])
                dist_dict[i].append((dist_curr, j))
                dist_dict[j].append((dist_curr, i))
        
        counter, visited, answer, heap = 1, [0] * n_points, 0, dist_dict[0]
        heapq.heapify(heap)
        visited[0] = 1
        
        while heap:
            dist_curr, point_curr = heapq.heappop(heap)
            
            if not visited[point_curr]:
                counter += 1
                visited[point_curr] = 1
                answer += dist_curr
                
                for candidate in dist_dict[point_curr]:
                    heapq.heappush(heap, candidate)
            
            if counter >= n_points:
                break
        return answer

        

