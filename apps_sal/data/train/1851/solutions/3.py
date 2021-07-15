class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        
        dp = [T+1] * (T+1)
        dp[0] = 0
        i = 1
        while i <= T and dp[i-1] < T:
            for c in clips:
                if c[0] <= i and i <= c[1]:
                    dp[i] = min(dp[i], dp[c[0]] + 1)
            i+=1
        return dp[T] if dp[T] != T+1 else -1
