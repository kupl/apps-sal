import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        visited = collections.defaultdict(int)
        N = len(graph)
        for i in range(N):
            if self.dfs(graph, i, visited):
                res.append(i)
        return res

    def dfs(self, graph, node, visited):
        if visited[node] == 1:
            return False
        if visited[node] == 2:
            return True
        visited[node] = 1
        for n in graph[node]:
            if not self.dfs(graph, n, visited):
                return False
        visited[node] = 2
        return True
