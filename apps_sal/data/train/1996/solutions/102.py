class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = [0 for _ in range(len(graph))]
        ans = []

        def dfs(cur):
            if v[cur] == 1:
                return True
            if v[cur] == 2:
                return False
            v[cur] = 1
            for j in graph[cur]:
                if dfs(j):
                    return True
            v[cur] = 2
            return False

        for i in range(len(graph)):
            if dfs(i):
                continue
            else:
                ans.append(i)

        return ans
