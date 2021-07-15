class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g = dict(enumerate(graph))
        
        safe = [-1] * len(g)
        
        def dfs(v):
            if safe[v] >= 0:
                return safe[v]
            
            if v not in g:
                safe[v] = 0
                return 0
            
            children = g.pop(v)
            
            if all(map(dfs, children)):
                safe[v] = 1
                return 1
            
            safe[v] = 0
            return 0
        
        for i in range(len(g)):
            dfs(i)
        
        return [i for i, s in enumerate(safe) if s > 0]
                
            
            # if (1) all of my children are safe
            # if (2) 
            
            
            
        
        

