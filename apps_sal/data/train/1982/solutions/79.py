
from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(dislikes)):
            graph[dislikes[i][0]].append(dislikes[i][1])
            graph[dislikes[i][1]].append(dislikes[i][0])

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(n, c ^ 1) for n in graph[node])

        return all(dfs(x) for x in range(1, N + 1) if x not in color)
