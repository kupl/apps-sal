from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        G, colors = defaultdict(list), defaultdict(lambda : 0)
        for u,v in dislikes:
            G[u].append(v)
            G[v].append(u)
        
        def dfs(u, color):
            if u in colors:
                return colors[u] == color
            colors[u] = color
            return all((dfs(v, -color) for v in G[u]))
        
        
        return all((dfs(v, 1) for v in range(1, N+1) if v not in colors))
        

