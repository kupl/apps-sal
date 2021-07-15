class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        m = len(graph)
        color = [0] * m
        def dfs(i):
            if color[i]:
                return color[i] == 1
            color[i] = 2
            for n in graph[i]:
                if not dfs(n):
                    return False
            color[i] = 1
            return True
        output = []
        for i in range(m):
            if dfs(i):
                output.append(i)
        return output
