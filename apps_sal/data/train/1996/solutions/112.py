class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:  
        # 0 = not processed     1 = processing     2 = processed
        
        def cycle(ind):
            if color[ind] == 1:
                return True   # true means that there is a cycle
            if color[ind] == 2:
                return False   # no cycle is present
            
            color[ind] = 1
            
            for node in graph[ind]:
                if cycle(node):
                    return True            
            color[ind] = 2
            return False
  
        
        n = len(graph)
        color = [0]*n  
        
        for i in range(len(graph)):
            cycle(i)     
        
        return [i for i in range(n) if color[i] == 2]
    
#     def helper(self, graph, index, visited, cache) -> bool:
#         if visited[index]:
#             return False
        
#         if len(graph[index]) == 0:
#             return True
        
#         if index in cache:
#             return cache[index]
        
#         visited[index] = True
#         safe = True
#         for v in graph[index]:
#             safe = safe and self.helper(graph, v, visited, cache)
#         visited[index] = False
        
#         cache[index] = safe
#         return safe
        
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         result = []
#         cache = {}
#         for i in range(len(graph)):
#             visited = [False for node in graph]
#             if self.helper(graph, i, visited, cache):
#                 result.append(i)
#         return result

