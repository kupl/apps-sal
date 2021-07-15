from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = defaultdict(list)
        n = len(points)
        for i in range(n-1):
            x,y = points[i]
            for j in range(i+1, n):
                u,v = points[j]
                d = abs(x-u) + abs(y-v)
                edges[d].append((i,j))
        find = {i:i for i in range(n)}
        union = {i:set([i]) for i in range(n)}
        cost = 0
        m = n-1
        min_edges = sorted(edges.keys())
        while m>0:
            d = min_edges.pop(0)
            j = 0
            while m>0 and j<len(edges[d]):
                u,v = edges[d][j]
                if find[u]!=find[v]:
                    x = min(find[u], find[v])
                    y = max(find[u], find[v])
                    
                    for z in union[y]:
                        find[z] = x
                    
                    union[x] = union[x] | union[y]
                    
                    cost += d
                    m -= 1
                j += 1
        return cost

