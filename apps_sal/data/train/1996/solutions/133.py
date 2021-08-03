class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        colour = [0] * len(graph)

        def dfs(i):
            if colour[i] != 0:
                return colour[i] == 2

            colour[i] = 1
            for c in graph[i]:
                if not dfs(c):
                    return False
            colour[i] = 2
            return True

        for node in range(len(graph)):
            dfs(node)
        return [i for i in range(len(graph)) if colour[i] == 2]
