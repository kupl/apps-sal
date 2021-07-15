class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        colour = [-1]*n
        
        def dfs(u):
            if colour[u]!=-1:
                colour[u]=1
            
            colour[u]=0
            for nei in graph[u]:
                if colour[nei]==1:
                    continue
                if colour[nei]==0 or not dfs(nei):
                    return False
            colour[u]=1
            return True
        
        return list(filter(dfs, list(range(n))))
                
            
        
        

