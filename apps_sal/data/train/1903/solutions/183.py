class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # turns out sorted + union find is the best
        # but makes sense to write union find using nonlocal as they are less
        # likely to TLE

        n = len(points)
        edges = []
        for i in range(n-1):
            for j in range(i+1,n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
                
        cost = 0
        found = 0
        parents = list(range(n))
        
        def find(a):
            while a != parents[a]:
                a, parents[a] = parents[a], parents[parents[a]]
            return a
        
        def union(a, b):
            parents[find(a)] = find(b)
        
        for c, a, b in sorted(edges):
            if find(a) != find(b):
                union(a,b)
                found += 1
                cost += c
                
            if found == n-1:
                break
        
        return cost
