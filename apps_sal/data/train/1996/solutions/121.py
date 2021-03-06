class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        (ans, dp, visited) = ([], {}, set())

        def dfs_visit(i):
            if i in visited:
                return False
            if i in dp:
                return dp[i]
            visited.add(i)
            valid = True
            if graph[i]:
                valid = all([dfs_visit(j) for j in graph[i]])
            visited.remove(i)
            dp[i] = valid
            return valid
        for i in range(len(graph)):
            if dfs_visit(i):
                ans.append(i)
        return ans
