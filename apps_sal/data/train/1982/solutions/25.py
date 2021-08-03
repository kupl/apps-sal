from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        edges = defaultdict(list)
        for p, c in dislikes:
            edges[p].append(c)
            edges[c].append(p)

        def dfs(i):
            colour = visited[i]
            for c in edges[i]:
                if c in visited:
                    if visited[c] != -colour:
                        return False
                else:
                    visited[c] = -colour
                    if not dfs(c):
                        return False
            return True

        visited = {}
        for i in range(1, N + 1):
            if i not in visited:
                visited[i] = 1
                if not dfs(i):
                    return False
        return True
