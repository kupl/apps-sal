class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()
        for i in range(len(graph)):
            visited = set([i])
            self.dfs(graph, i, visited, res)
        
        return sorted(list(res))
    
    # dfs is to check if there's a cycle starting from this point
    def dfs(self, graph, i, visited, res):
        for j in graph[i]:
            if j in visited:
                return False
            # This step is not necessary for the correctness of the result, but saves time
            if j in res:
                continue
            visited.add(j)
            # Now we go on to the next step and see if there's a cycle
            if not self.dfs(graph, j, visited, res):
                return False
            visited.remove(j)
        
        res.add(i)
        return True
            

