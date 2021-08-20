class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        def dfs(i):
            if color[i] == 1:
                return False
            elif color[i] == 2:
                return True
            elif color[i] == 0:
                color[i] = 1
                for j in graph[i]:
                    if not dfs(j):
                        return False
                color[i] = 2
                ans.append(i)
                return True
        ans = []
        color = [0] * len(graph)
        for i in range(len(graph)):
            if color[i] == 0:
                dfs(i)
        return sorted(ans)
