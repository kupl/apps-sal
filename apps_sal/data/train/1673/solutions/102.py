class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        N = len(arr)

        dp = [[0] * N for _ in range(N)]

        for i in range(N):
            dp[N - 1][i] = arr[N - 1][i]

        for r in range(N - 2, -1, -1):
            for c in range(N):
                min_c = float('inf')
                for n_c in range(N):
                    if n_c == c:
                        continue
                    min_c = min(min_c, arr[r + 1][n_c])
                dp[r][c] = min_c + arr[r][c]
                arr[r][c] = dp[r][c]

        res = float('inf')
        for i in range(N):
            res = min(res, dp[0][i])

        return res
