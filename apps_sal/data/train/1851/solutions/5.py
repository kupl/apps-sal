class Solution:

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [T + 1] * (T + 1)
        dp[0] = 0
        for i in range(1, T + 1):
            if dp[i - 1] >= T:
                break
            for (start, end) in clips:
                if start <= i <= end:
                    dp[i] = min(dp[i], dp[start] + 1)
                    print(dp)
        if dp[T] == T + 1:
            return -1
        else:
            return dp[T]
