from collections import defaultdict


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        def calc_distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return abs(x1 - x2) + abs(y1 - y2)
        
        def find_best_node(min_dists, mst_set):
            min_dist = float('inf')
            for i, dist in enumerate(min_dists):
                if i not in mst_set and dist < min_dist:
                    best_node = i
                    min_dist = dist
            return best_node, min_dist
        
        def update_min_dists(node, min_dists, graph):
            for i, dist in graph[node]:
                min_dists[i] = min(min_dists[i], dist)            
        
        
        n = len(points)
        if n <= 1:
            return 0
        
        graph = defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                p1, p2 = points[i], points[j]
                dist = calc_distance(p1, p2)
                graph[i].append((j, dist))
                graph[j].append((i, dist))
                
        min_dists = [float('inf') for _ in range(n)]
        mst_set = {0}
        for i, dist in graph[0]:
            min_dists[i] = min(min_dists[i], dist)
        
        total_dist = 0
        for _ in range(n-1):
            best_node, min_dist = find_best_node(min_dists, mst_set)
            mst_set.add(best_node)
            update_min_dists(best_node, min_dists, graph)
            total_dist += min_dist
        
        return total_dist
            
            
            
        
        
        
        
            
        
        

