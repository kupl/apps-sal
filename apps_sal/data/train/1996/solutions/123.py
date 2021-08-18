class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [-1] * n
        result = []

        def dfs(node):
            state[node] = 0
            for adj in graph[node]:
                if state[adj] == 0 or (state[adj] == -1 and dfs(adj)):
                    return True
            state[node] = 1
            result.append(node)

        for i in range(n):
            if state[i] == -1:
                dfs(i)

        return sorted(result)
