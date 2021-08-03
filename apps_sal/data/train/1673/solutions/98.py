from functools import lru_cache


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j):
            if not (0 <= i < len(arr) and 0 <= j < len(arr[0])):
                return float('inf')
            if i == len(arr) - 1:
                return arr[i][j]
            return arr[i][j] + min(dp(i + 1, k) for k in range(len(arr[0])) if k != j)

        return min(dp(0, j) for j in range(len(arr[0])))
