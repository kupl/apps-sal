class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        n = len(clips)
        dp = [float('inf')] * (T + 1)
        dp[0] = 0
        for i in range(1, T + 1):
            for j in range(n):
                if clips[j][0] <= i <= clips[j][1]:
                    dp[i] = min(dp[i], 1 + dp[clips[j][0]])
        if dp[T] == float('inf'):
            return -1
        return dp[-1]
