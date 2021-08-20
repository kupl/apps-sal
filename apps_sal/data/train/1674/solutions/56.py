from functools import lru_cache


class Solution:

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @lru_cache(maxsize=None)
        def dfs(index, M):
            if 2 * M >= n - index:
                return sum(piles[index:])
            ret = float('inf')
            for X in range(1, 2 * M + 1):
                if X > n - index:
                    break
                ret = min(ret, dfs(index + X, max(X, M)))
            return sum(piles[index:]) - ret
        return dfs(0, 1)
