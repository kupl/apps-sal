class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # for each point, you need to find the nearest point 
        import heapq
        
        graph = self.build_graph(points)
        min_heap = []
        start = 0
  
        for dist, node in graph[start]:
            heapq.heappush(min_heap, (dist, node))
        
        visited = set()
        visited.add(start)
        res = cnt = 0
        
        while len(min_heap) > 0:
            dist, node = heapq.heappop(min_heap)
            if cnt == len(points) - 1:
                break
            
            if node not in visited:
                res += dist 
                cnt += 1 
                visited.add(node)
                for nxt_dist, nxt_node in graph[node]:
                    heapq.heappush(min_heap, (nxt_dist, nxt_node)) 
            
        return res
    
    def build_graph(self, points):
        from collections import defaultdict
        graph = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                graph[i].append((self.dist(points[i], points[j]), j))
        return graph
                
    
    def dist(self, p0, p1):
        x0, y0 = p0
        x1, y1 = p1
        return abs(x1 - x0) + abs(y1 - y0)
