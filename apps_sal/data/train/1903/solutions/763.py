# kruskal 
class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:                        
        n, q = len(a), []
        for i in range(n-1):
            for j in range(i+1, n):
                q.append((abs(a[i][0]-a[j][0]) + abs(a[i][1]-a[j][1]), i, j))
                        
        def union(u, v):
            UF[find(v)] = UF[find(u)]
        def find(u):
            if u != UF[u]: UF[u] = find(UF[u])
            return UF[u]
        
        heapify(q)
        ans, vis, UF = 0, set(), {i: i for i in range(n)}
        while q and len(set(find(u) for u in UF)) != 1:
            val, i, j = heappop(q)
            if find(i) != find(j):
                union(i, j)
                vis |= set([i, j])
                ans += val
        return ans                        
