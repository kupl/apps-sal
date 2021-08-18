from functools import lru_cache


class Solution:
    def countRoutes(self, locations, start: int, finish: int, fuel: int) -> int:
        @lru_cache(None)
        def dfs(s, f):
            if f < 0:
                return 0
            res = 0
            if s == finish:
                res += 1
            for e in range(length):
                if s != e:
                    res += dfs(e, f - matrix[s][e])
            return res % M

        M = 10**9 + 7
        length = len(locations)
        matrix = [[0] * length for _ in range(length)]
        for i in range(length):
            for j in range(length):
                matrix[i][j] = matrix[j][i] = abs(locations[i] - locations[j])

        return dfs(start, fuel) % M
