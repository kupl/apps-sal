from collections import defaultdict
import heapq

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
                
        total_dist = 0
        visited = [False] * n_points
        counter = 1
        dist_heap = dist_dict[0]
        heapq.heapify(dist_heap)
        visited[0] = True
        
        while dist_heap:
            dist_curr, point_curr = heapq.heappop(dist_heap)
            if not visited[point_curr]:
                visited[point_curr] = True
                for neighbor in dist_dict[point_curr]:
                    heapq.heappush(dist_heap, neighbor)
                total_dist += dist_curr
                counter += 1
            if counter >= n_points: break
         
        return total_dist
                
            
            
            

