class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}
        departures = [-1] * len(graph)
        res = []

        def _dfs(node):
            visited[node] = 1
            neighbors = graph[node]
            for neighbor in neighbors:
                if neighbor not in visited:
                    if _dfs(neighbor):
                        return True
                elif departures[neighbor] == -1:
                    return True
            departures[node] = 1
            return False
        for i in range(0, len(graph)):
            if not _dfs(i):
                res.append(i)
        return res
