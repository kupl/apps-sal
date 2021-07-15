from collections import defaultdict
class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
       
        g = defaultdict(list)    
        for x, y in dislikes:
            g[x].append(y)
            g[y].append(x)
            
        groups = {}
        def dfs(curr, i):
            if curr in groups:
                return groups[curr] == i
            
            groups[curr] = i
            return all(dfs(nb, not i) for nb in g[curr])
        
        return all(dfs(x, groups.get(x, False)) for x, _ in dislikes)
