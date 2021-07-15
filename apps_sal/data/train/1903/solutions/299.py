class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1: return 0
        
        # Kruskal's algorithm
        
        # Sort the edges by cost
        edges = []
        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        
        # Union find utility
        roots = [i for i in range(N)]
        def find(i):
            if roots[i] != i:
                roots[i] = find(roots[i])
            return roots[i]
    
        def join(i, j):
            ri, rj = find(i), find(j)
            roots[ri] = rj
            
        i = cnt = 0
        res = 0
        while cnt < N - 1:
            d, x, y = edges[i]
            i += 1
            rx, ry = find(x), find(y)
            if find(x) == find(y): # If already connected, cannot use this edge
                continue
            join(rx, ry)
            cnt += 1
            res += d
        return res
