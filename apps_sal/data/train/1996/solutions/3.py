from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph):
        state = defaultdict(lambda: 'unknown')

        def dfs(node):
            if state[node] != 'unknown':
                return state[node] == 'safe'
            state[node] = 'visiting'
            for nei in graph[node]:
                if state[nei] == 'visiting' or not dfs(nei):
                    return False
            state[node] = 'safe'
            return True
        N = len(graph)
        return [node for node in range(N) if dfs(node)]
