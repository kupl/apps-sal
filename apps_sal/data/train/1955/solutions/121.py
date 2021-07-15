class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        def dfs(node):
            seen.add(node)
            idx.append(node)
            ch.append(s[node])
            
            for nei in graph[node]:
                if nei not in seen:
                    dfs(nei)
            
        
        
        graph = collections.defaultdict(list)
        
        for u, v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        
        seen = set()
        idxCh = [\"\"]*len(s)
        
        for i in range(len(s)):
            if i not in seen:
                idx = []
                ch = []
                dfs(i)
            for i, c in zip(sorted(idx), sorted(ch)):
                idxCh[i] = c
        return \"\".join(idxCh)
            
        
     #    0 - 3
     #    |
     #1 - 2
    
    # [0,3] bd
    # [1,2] ac
    
    
