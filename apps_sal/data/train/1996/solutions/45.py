class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        def cycle(index):
            if visited[index] == 1:
                return True
            if visited[index] == 2:
                return False
            
            visited[index] = 1
            for node in graph[index]:
                if cycle(node):
                    return True
                
            visited[index] = 2
            return False
        
        
        visited = [0] * len(graph)
        
        for i in range(len(graph)):
            cycle(i)
                    
        safe = []
        for i in range(len(graph)):
            if visited[i] == 2:
                safe.append(i)
        return safe
