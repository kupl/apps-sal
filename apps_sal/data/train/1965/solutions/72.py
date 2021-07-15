class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        d_alice = {i: i for i in range(1, n + 1)}
        d_bob = {i: i for i in range(1, n + 1)}
        
        def find(d, ind):
            if d[ind] != ind:
                d[ind] = find(d, d[ind])
            return d[ind]
        
        def union(d, i1, i2):
            d[find(d, i1)] = find(d, i2)
        
        edges.sort(reverse=True)
        res = 0
        
        for typ, i, j in edges:
            if typ == 3:
                if find(d_alice, i) == find(d_alice, j) and find(d_bob, i) == find(d_bob, j):
                    res += 1
                    continue
                union(d_alice, i, j)
                union(d_bob, i, j)
            elif typ == 2:
                if find(d_alice, i) == find(d_alice, j):
                    res += 1
                    continue
                union(d_alice, i, j)
            else:
                if find(d_bob, i) == find(d_bob, j):
                    res += 1
                    continue
                union(d_bob, i, j)
                
        for i in range(2, n + 1):
            if find(d_alice, i) != find(d_alice, i-1) or find(d_bob, i) != find(d_bob, i-1):
                return -1
        
        return res

