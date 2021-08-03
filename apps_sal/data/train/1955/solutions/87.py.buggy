class Solution:
    # 21:50
    \"\"\"
    s = \"dcab\", pairs = [[0,3],[1,2],[0,2]]
    dcab -[1, 2]->dacb
    dacb -[0, 3]->bacd
    not possible anymore
    \"\"\"
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        res = list(s)
        adj = collections.defaultdict(set)
        for a, b in pairs:
            adj[a].add(b)
            adj[b].add(a)
            
        def dfs(i, v):
            if i in adj:
                v.append(i)
                for j in adj.pop(i):
                    dfs(j, v)
            
            
        while adj:
            i = next(iter(adj))
            v = []
            dfs(i, v)
            v = sorted(v)
            chars = sorted([s[i] for i in v])
            for i, c in enumerate(chars):
                res[v[i]] = c
                
        return ''.join(res)
    
        
                
        
