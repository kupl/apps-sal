class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(p, i):
            if p[i] != i:
                p[i] = find(p, p[i])
            return p[i]
        
        def union(p, i, j):
            p[find(p, i)] = find(p, j)
        
        parents = list(range(n))
        ans = 0
        
        edges = [(type, u - 1, v - 1) for type, u, v in edges]
        
        for type, u, v in edges:
            if type == 3:
                if find(parents, u) == find(parents, v):
                    ans += 1
                union(parents, u, v)
        
        alice = list(parents)
        bob = list(parents)
        
        for type, u, v in edges:
            if type == 1:
                if find(alice, u) == find(alice, v):
                    ans += 1
                union(alice, u, v)
            if type == 2:
                if find(bob, u) == find(bob, v):
                    ans += 1
                union(bob, u, v)
        
        return ans if len({find(alice, i) for i in range(n)}) == 1 and len({find(bob, i) for i in range(n)}) == 1 else -1
        
                    

