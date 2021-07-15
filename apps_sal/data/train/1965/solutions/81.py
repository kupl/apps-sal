class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(i, parents):
            if parents[i] != i:
                parents[i] = find(parents[i], parents)
            return parents[i]
            
        def union(i, j, parents, groups):
            p_i = find(i, parents)
            p_j = find(j, parents)
            if p_i != p_j:
                groups -= 1
                if p_i > p_j:
                    parents[p_j] = p_i
                else:
                    parents[p_i] = p_j
            return groups
        
        alice = []
        bob = []
        res = 0
        
        parents = list(range(n+1))
        groups = n  
        
        for t, a, b in edges:
            if t == 1:
                alice.append((a, b))
            elif t == 2:
                bob.append((a, b))
            else:
                if find(a, parents) == find(b, parents):
                    res += 1
                else:
                    groups = union(a, b, parents, groups)
                    
        if groups == 1:
            return res + len(alice) + len(bob)
        
        ga = groups
        gb = groups
        pa = parents[:]
        pb = parents[:]
        
        while alice:
            i, j = alice.pop()
            if find(i, pa) == find(j, pa):
                res += 1
            else:
                ga = union(i, j, pa, ga)
            if ga == 1:
                res += len(alice)
                break
                
        if ga != 1:
            return -1
        
        while bob:
            i, j = bob.pop()
            if find(i, pb) == find(j, pb):
                res += 1
            else:
                gb = union(i, j, pb, gb)
            if gb == 1:
                res += len(bob)
                break
                
        if gb != 1:
            return -1
        
        return res
        
            

