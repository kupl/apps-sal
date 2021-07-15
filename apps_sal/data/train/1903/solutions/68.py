class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        edges = []
        N = len(points)
        parent = [x for x in range(N)]
        rank = [1 for x in range(N)]
        
        def ufind(x):
            if parent[x] == x:
                return parent[x]
            return ufind(parent[x])
            
        def uunion(x, y):
            ux = ufind(x)
            uy = ufind(y)
            if rank[ux] > rank[uy]:
                parent[uy] = ux
                rank[ux] += rank[uy]
            else:
                parent[ux] = uy
                rank[uy] += rank[ux]
            
        def dist(xi, yi, xj, yj):
            return abs(xi-xj) + abs(yi-yj)
        
        for i in range(N):
            xi, yi = points[i]
            for j in range(i+1, N):
                xj, yj = points[j]
                edges.append((dist(xi, yi, xj, yj), i, j))
                
        heapq.heapify(edges)
        
        for v in range(len(edges)):
            edge, i, j = heapq.heappop(edges)
            if ufind(i) != ufind(j):
                uunion(i, j)
                total += edge
        # for edge, i, j in edges:
        #     if ufind(i) != ufind(j):
        #         uunion(i, j)
        #         total += edge
        
        return total
