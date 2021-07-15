class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def manhattan_distance(point_1, point_2):
            x1, y1 = point_1
            x2, y2 = point_2
            return abs(x2 - x1) + abs(y2 - y1)
        
        n = len(points)
        graph = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                dist = manhattan_distance(points[i], points[j])
                graph[i].append((dist, j))
                graph[j].append((dist, i))
            
        visited = set()
        visited.add(0)
        heap = [_ for _ in graph[0]]
        heapq.heapify(heap)
        cost = 0
        
        while heap and len(visited) != len(points):
            dist, neighbor = heapq.heappop(heap)
            if neighbor not in visited:
                visited.add(neighbor)
                cost += dist
                for new_dist, new_neighbor in graph[neighbor]:
                    if new_neighbor not in visited:
                        heapq.heappush(heap, (new_dist, new_neighbor))
                        
        return cost
    
    
    
    
    
    
    
    
    
    
    
    

