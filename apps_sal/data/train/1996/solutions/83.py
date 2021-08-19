# visiting, safe, unsafe
from collections import defaultdict


class Solution:
    def eventualSafeNodes(self, graph):
        state = defaultdict(int)

        def dfs(node):
            if state[node] == 1:
                state[node] = 3
                return 3
            if state[node]:
                return state[node]
            state[node] = 1
            for nei in graph[node]:
                if dfs(nei) == 3:
                    state[node] = 3
                    return 3
            state[node] = 2
            return 2
        N = len(graph)
        return [node for node in range(N) if dfs(node) == 2]
