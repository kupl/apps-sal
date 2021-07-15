class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        terminal = []
        n = len(graph)
        visited = [-1]*n
        
                
        def dfs(i):
            visited[i] = 0 # i is visiting
            for t in graph[i]:
                if visited[t] == 0 or (visited[t]==-1 and not dfs(t)):
                    return False
            visited[i] = 1 # i visited already
            terminal.append(i)
            return True
                
        for i in range(n):
            if visited[i] == -1:
                dfs(i)
                
        return sorted(terminal)
