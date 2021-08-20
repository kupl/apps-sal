class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        g = [[] for _ in range(N)]
        for p in dislikes:
            p[0] -= 1
            p[1] -= 1
            g[p[0]].append(p[1])
            g[p[1]].append(p[0])
        col = [0] * N

        def dfs(v, c):
            col[v] = c
            for to in g[v]:
                if col[to] == c:
                    return False
                elif col[to] == 0 and (not dfs(to, 3 - c)):
                    return False
            return True
        for i in range(N):
            if col[i] == 0 and (not dfs(i, 1)):
                return False
        return True
