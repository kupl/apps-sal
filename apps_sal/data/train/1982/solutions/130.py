from collections import defaultdict


class Solution:

    def possibleBipartition(self, N, dislikes):
        G = defaultdict(set)
        for (u, v) in dislikes:
            G[u].add(v)
            G[v].add(u)
        color = dict()

        def dfs(node, c):
            if node in color:
                return color[node] == c
            color[node] = c
            return all((dfs(nei, c ^ 1) for nei in G[node]))
        return all((dfs(node, 0) for node in range(1, N + 1) if node not in color))
