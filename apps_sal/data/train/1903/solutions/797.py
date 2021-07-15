class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                # if i != j:
                x1,y1 = points[i]
                x2,y2 = points[j]
                md = abs(x1-x2)+abs(y1-y2)

                graph[i].append((md, j))
                graph[j].append((md, i))
                    
        visited = set()
        heap = [(0, 0)]
        mx = 0
        
        while heap:
            distance, node = heapq.heappop(heap)
            
            if node not in visited:
                
                visited.add(node)
                mx += distance

                for dis, neigh in graph[node]:
                    if neigh not in visited:
                        heapq.heappush(heap, (dis,neigh))
                        
        return mx


