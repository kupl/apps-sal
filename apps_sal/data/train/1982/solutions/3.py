class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        color = {}
        for i in range(1, N + 1):
            if i not in color:
                ret = self.dfs(graph, i, color, 'R')
                if not ret:
                    return False
        return True

    def dfs(self, graph, i, color, currentColor) -> bool:
        color[i] = currentColor
        complementaryColor = 'R' if currentColor == 'B' else 'B'
        for neighbor in graph[i]:
            if neighbor in color:
                if color[neighbor] == currentColor:
                    return False
            else:
                res = self.dfs(graph, neighbor, color, complementaryColor)
                if not res:
                    return False
        return True
