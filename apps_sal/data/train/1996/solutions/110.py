class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0] * n

        def dfs(node):
            if color[node]:
                return color[node] == 2
            color[node] = 1
            for nbor in graph[node]:
                if not dfs(nbor):
                    return False
            color[node] = 2
            return True
        return [node for node in range(n) if dfs(node)]
