from collections import defaultdict


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        groups = defaultdict(list)
        for (a, b) in dislikes:
            groups[a].append(b)
            groups[b].append(a)
        colors = {}

        def dfs(node, c=0):
            if node in colors:
                return colors[node] == c
            colors[node] = c
            return all((dfs(nei, 1 - c) for nei in groups[node]))
        return all((dfs(node) for node in range(1, N + 1) if node not in colors))
