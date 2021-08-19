class Solution:

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [float(inf)] * 101
        clips.sort()
        if clips[0][0] > 0:
            return -1
        dp[0] = 0
        for i in range(len(clips)):
            clip = clips[i]
            if clip[0] != 0 and dp[clip[0]] == float(inf):
                break
            min_so_far = dp[clip[0]]
            for k in range(clip[0], clip[1] + 1):
                dp[k] = min(dp[k], min_so_far + 1)
        if dp[T] == inf:
            return -1
        return dp[T]
