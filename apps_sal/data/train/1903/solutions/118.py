class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(p, u):
            if p[u] == u:
                return u
            root_u = find(p, p[u])
            p[u] = root_u
            return root_u
        
        def union(p, rank, root_u, root_v):
            if rank[root_u] < rank[root_v]:
                p[root_u] = root_v
            elif rank[root_v] < rank[root_u]:
                p[root_v] = root_u
            else:
                rank[root_u] += 1
                p[root_v] = root_u
            
        
        h = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(h, [cost, i, j])
        
        p = list(range(len(points)))
        rank = [1] * len(points)
        total_cost = 0
        while len(h):
            cost, u, v = heapq.heappop(h)
            root_u, root_v = find(p, u), find(p, v)
            if root_u == root_v:
                continue
            union(p, rank, root_u, root_v)
            total_cost += cost
    
        return total_cost
            
            
        
                
                    

