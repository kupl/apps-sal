class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                x1,y1 = points[i]
                x2,y2 = points[j]
                manhattan_dist = abs(x1-x2)+abs(y1-y2)

                graph[i].append((manhattan_dist, j))
                graph[j].append((manhattan_dist, i))
                    
        visited = set()
        heap = [(0, 0)]
        cost = 0
        
        while heap:
            distance, current_node = heapq.heappop(heap)
            
            if current_node not in visited:
                
                visited.add(current_node)
                cost += distance

                for dist, neigh in graph[current_node]:
                    if neigh not in visited:
                        heapq.heappush(heap, (dist,neigh))
                        
        return cost
