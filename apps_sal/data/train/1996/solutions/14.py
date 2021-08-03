from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph):
        state = defaultdict(int)

        def dfs(node):
            if state[node]:
                return state[node] == 2
            state[node] = 1
            for nei in graph[node]:
                if state[nei] == 1 or not dfs(nei):
                    return False
            state[node] = 2
            return True
        N = len(graph)
        return [node for node in range(N) if dfs(node)]
