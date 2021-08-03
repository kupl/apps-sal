class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N == 1 or not dislikes:
            return True

        g = defaultdict(set)
        for a, b in dislikes:
            g[a].add(b)
            g[b].add(a)

        color = [-1] * (N + 1)

        def dfs(i, c):
            color[i] = c
            for nxt in g[i]:
                if color[nxt] != -1 and color[nxt] == c:
                    return False
                if color[nxt] == -1 and not dfs(nxt, c ^ 1):
                    return False
            return True

        for i in range(1, N + 1):
            if color[i] == -1 and not dfs(i, 0):
                return False

        return True
