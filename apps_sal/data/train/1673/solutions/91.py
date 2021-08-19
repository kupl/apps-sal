class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0:
                return arr[0][j]
            if i == len(arr):
                return min((dp(i - 1, k) for k in range(len(arr[0]))))
            return arr[i][j] + min((dp(i - 1, k) for k in range(len(arr[0])) if k != j))
        return dp(len(arr), -1)
