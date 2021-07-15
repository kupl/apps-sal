class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # build graph, use type 3 first
        # then do alice and bob separately
        # have dsu parents to build up alice and bob
        
        parentsA = list(range(n))
        parentsB = list(range(n))
        
        def find(parents, a):
            while a != parents[a]:
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a
            
        def union(parents, a, b):
            a = find(parents, a)
            b = find(parents, b)
            parents[a] = b
        
        type3 = []
        typeB = []
        typeA = []
        
        for t, u, v in edges:
            u, v = u-1, v-1 # make zero indexed, easier for UF
            if t == 3:
                type3.append((u, v))
            elif t == 2:
                typeB.append((u, v))
            elif t == 1:
                typeA.append((u, v))
                
        # now add type3 edges if they join together two new things
        
        tree1, tree2, res = 0,0,0
        for u, v in type3:
            if find(parentsA, u) != find(parentsA, v):
                tree1 += 1
                tree2 += 1
                union(parentsA, u, v)
                union(parentsB, u, v)
            else:
                res += 1
                
        # now do type1 and 2 separately
        for u,v in typeA:
            if find(parentsA, u) != find(parentsA, v):
                tree1 += 1
                union(parentsA, u, v)
            else:
                res += 1
        
        for u,v in typeB:
            if find(parentsB, u) != find(parentsB, v):
                tree2 += 1
                union(parentsB, u, v)
            else:
                res += 1
        
        if tree1 == n-1 and tree2 == n-1:
            return res
        else:
            return -1
