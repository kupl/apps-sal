class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(graph, node):
            if not graph[node]:
                return True
            if node not in self.dp:
                self.dp[node] = -1
                res = True
                for nex in graph[node]:
                    res = res and dfs(graph, nex)
                self.dp[node] = res
            else:
                if self.dp[node] == -1:
                    return False
            return self.dp[node]
        
        self.dp = {}
        res = []
        for i in range(len(graph)):
            if dfs(graph, i):
                res.append(i)
        return res

