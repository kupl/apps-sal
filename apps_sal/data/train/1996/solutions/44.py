class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        WHITE, GRAY, BLACK = 0, 1, 2    #GRAY is part of a cycle, BLACK is safe
        color = {}
        for i in range(len(graph)):
            color[i] = WHITE
         
        # Return whether it is safe
        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK
            
            color[node] = GRAY
            for nei in graph[node]:
                if color[nei] == BLACK:
                    continue
                elif color[nei] == GRAY:
                    return False
                elif not dfs(nei):
                    return False
            color[node] = BLACK
            return True
        
        safe = []
        for i in range(len(graph)):
            if dfs(i):
                safe.append(i)
                
        return safe
            
            
            
            
        
        
        

