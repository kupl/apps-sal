class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        \"\"\"
        Just move along unvisited (-1) nodes and remark them as 0 on the queue while visiting others on the path and finish them as 1. If you meet them again on the queue while visiting (being 0) it means you completed a cycle, in other words it is not safe and return back without adding.
        \"\"\"
        visited, result = [-1] * len(graph), []
        
        def explore(i):
            visited[i] = 0
            for v in graph[i]:
                if visited[v] == 0 or (visited[v]==-1 and explore(v)): return True
            visited[i] = 1
            result.append(i)
            return False
        
        for i in range(len(graph)):
            if visited[i] == -1: explore(i)

        return sorted(result)
            
