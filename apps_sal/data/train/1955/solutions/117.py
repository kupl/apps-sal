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
            chars = sorted([s[i] for i in g])
            j = 0
            for i in g:
                res[i] = chars[j]
                j += 1
                
        return ''.join(res)
    
    def groups(self, pairs, n):
        adj = collections.defaultdict(set)
        for p in pairs:
            adj[p[0]].add(p[1])
            adj[p[1]].add(p[0])
            
        arr = []
        while adj:
            i = list(adj.keys())[0]
            v = []
            self.dfs(i, adj, v)
            arr.append(sorted(list(v)))
                
        return arr
    
    def dfs(self, i, adj, res):
        if i in adj:
            res.append(i)
            for j in adj.pop(i):
                self.dfs(j, adj, res)
        
                
        
