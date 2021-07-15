class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf1 = list(range(n+1))
        uf2 = list(range(n+1))
        uf3 = list(range(n+1))
        
        def find(uf, x):
            if x != uf[x]:
                uf[x] = find(uf, uf[x])
            return uf[x]
        
        def union(uf, x, y):
            uf[find(uf, x)] = find(uf, y)
            
        res = 0
        for t, u, v in edges:
            if t == 3 and find(uf3, u) != find(uf3, v):
                union(uf1, u, v)
                union(uf2, u, v)
                union(uf3, u, v)
                res += 1
                
        for t, u, v in edges:
            if t == 1 and find(uf1, u) != find(uf1, v):
                union(uf1, u, v)
                res += 1
            if t == 2 and find(uf2, u) != find(uf2, v):
                union(uf2, u, v)
                res += 1
                    
        if len({find(uf1, i) for i in range(1,n+1)}) > 1:
            return -1
        if len({find(uf2, i) for i in range(1,n+1)}) > 1:
            return -1
                    
        return len(edges) - res
