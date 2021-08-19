class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        ans = []

        def dfs(node):
            if arr[node] != -1:
                return arr[node] == 1
            arr[node] = 0
            for j in graph[node]:
                if arr[j] == 1:
                    continue
                elif arr[j] == 0 or not dfs(j):
                    return False
            arr[node] = 1
            return True
        arr = [-1] * n
        for i in range(n):
            if len(graph[i]) == 0:
                ans.append(i)
                continue
            if dfs(i):
                ans.append(i)
        return ans
