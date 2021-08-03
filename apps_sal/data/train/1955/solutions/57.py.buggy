class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        root = { i:i for i in range(n) }
        
        def find(i): # path compression
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]
            
            
        def union(i,j):
            ri = find(i)
            rj = find(j)
            if ri != rj:
                # root[j] = root[i]
                root[ri] = root[rj] # root(rj)
            return
        
        for i,j in pairs:
            union(i,j)
        
        d = collections.defaultdict( list )
        for i in range(n):
            d[find(i)].append(i)
        
        print(root)
        
        res = list(s)
        for k in d:
            tmp = sorted([s[i] for i in d[k]])
            for i in range(len(tmp)):
                res[ d[k][i] ] = tmp[i]
        
        return \"\".join(res)
        
        
        
        
        
