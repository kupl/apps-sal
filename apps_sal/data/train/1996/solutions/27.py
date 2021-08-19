class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()
        for i in range(len(graph)):
            visited = set([i])
            self.dfs(graph, i, visited, res)
        return sorted(list(res))

    def dfs(self, graph, i, visited, res):
        for j in graph[i]:
            if j in visited:
                return False
            if j in res:
                continue
            visited.add(j)
            if not self.dfs(graph, j, visited, res):
                return False
            visited.remove(j)
        res.add(i)
        return True
