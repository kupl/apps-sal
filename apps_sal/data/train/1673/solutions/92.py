class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        @functools.lru_cache(None)
        def dp(i, j):
            if i == 0: return arr[0][j]
            return arr[i][j] + min(dp(i-1, k) for k in range(len(arr[0])) if k!=j)
        return min(dp(len(arr)-1, i) for i in range(len(arr[0])))
