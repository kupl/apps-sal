class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        new_g = {i: [] for i in range(len(graph))}
        for (i, n) in enumerate(graph):
            new_g[i].append(n)

        def dfs(n):
            if status[n] == -1:
                return False
            if status[n] == 1:
                return True
            status[n] = -1
            for adj in graph[n]:
                if not dfs(adj):
                    return False
            status[n] = 1
            return True
        status = [0 for _ in range(len(graph))]
        return filter(dfs, range(len(graph)))
