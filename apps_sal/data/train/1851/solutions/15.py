class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: x[0])
        dp = [[0] * (len(clips) + 1)] + [[float('inf')] * (len(clips) + 1) for _ in range(T)]
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                dp[row][col] = dp[row][col - 1]
                if(clips[col - 1][0] <= row - 1 < clips[col - 1][1]):
                    dp[row][col] = min(dp[row][col], 1 + dp[clips[col - 1][0]][col])
        ans = dp[-1][-1] if dp[-1][-1] != float('inf') else -1
        return ans
