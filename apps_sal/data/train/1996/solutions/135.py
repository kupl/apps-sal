class Solution:

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        color = [0 for _ in range(n)]
        res = []
        for node_index in range(n):
            if self.dfs(graph, index=node_index, color=color):
                res.append(node_index)
        return res

    def dfs(self, graph, index, color):
        if color[index] > 0:
            return color[index] == 2
        color[index] = 1
        for j in graph[index]:
            if color[j] == 2:
                continue
            elif color[j] == 1 or not self.dfs(graph, j, color):
                return False
        color[index] = 2
        return True
