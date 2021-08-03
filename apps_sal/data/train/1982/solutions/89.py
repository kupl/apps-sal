class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        colour = [None] * (N + 1)
        graph = [[] for i in range(N + 1)]

        for v, u in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, col):
            nonlocal colour
            nonlocal graph
            if not colour[node]:
                colour[node] = col
            elif colour[node] == col:
                return True
            else:
                return False
            for i in graph[node]:
                if not dfs(i, (col + 1) % 2):
                    return False
            return True
        for i in range(1, N + 1):
            if not colour[i] and not dfs(i, 0):
                return False
        return True
