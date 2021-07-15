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
        groups = self.groups(pairs, len(s))
        for g in groups:
            g = sorted(g)
            chars = sorted([s[i] for i in g])
            for i, c in enumerate(chars):
                res[g[i]] = c
                
        return ''.join(res)
    
    def groups(self, pairs, n):
        adj = collections.defaultdict(set)
        for p in pairs:
            adj[p[0]].add(p[1])
            adj[p[1]].add(p[0])
            
        arr = []
        while adj:
            i = next(iter(adj))
            v = []
            self.dfs(i, adj, v)
            arr.append(v)
                
        return arr
    
    def dfs(self, i, adj, res):
        if i in adj:
            res.append(i)
            for j in adj.pop(i):
                self.dfs(j, adj, res)
        
                
        
