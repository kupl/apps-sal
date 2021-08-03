from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for u, v in dislikes:
            adj[u].append(v)
            adj[v].append(u)
        colors = {}

        def dfs(node, color):
            if node in colors:
                return colors[node] == color
            colors[node] = color
            return all(dfs(u, 1 - color) for u in adj[node])
        return all(dfs(u, 0) for u in range(1, N + 1) if u not in colors)
