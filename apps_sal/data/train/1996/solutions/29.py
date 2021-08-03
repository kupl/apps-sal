class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = set()
        for i in range(len(graph)):
            visited = set()
            self.dfs(graph, i, visited, res)

        return sorted(list(res))

    # dfs is to check if there's a cycle starting from this point
    def dfs(self, graph, i, visited, res):
        visited.add(i)
        for j in graph[i]:
            if j in visited:
                return False
            if j in res:
                continue
            if not self.dfs(graph, j, visited, res):
                return False
        visited.remove(i)
        res.add(i)
        return True
