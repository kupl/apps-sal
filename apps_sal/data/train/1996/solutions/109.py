class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        if len(graph) == 0:
            return ans
        status = [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            if status[i] == 0:
                self.dfs(i, graph, status, ans)
        for i in range(len(graph)):
            if status[i] == 2:
                ans.append(i)
        return ans

    def dfs(self, i, graph, status, ans):
        status[i] = 1
        for neighbor in graph[i]:
            if status[neighbor] == 1:
                return False
            if status[neighbor] == 0 and not self.dfs(neighbor, graph, status, ans):
                return False

        status[i] = 2
        return True
