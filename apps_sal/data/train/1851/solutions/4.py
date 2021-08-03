class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: x[0])
        n = len(clips)
        memo = {}

        def recur(i, interval):
            if (i, interval) in memo:
                return memo[(i, interval)]
            if interval >= T:
                return 0
            if i == n:
                return sys.maxsize
            if interval >= clips[i][0] and interval < clips[i][1]:
                ans = min(recur(i + 1, clips[i][1]) + 1, recur(i + 1, interval))
            else:
                ans = recur(i + 1, interval)
            memo[(i, interval)] = ans
            return ans
        fnl = recur(0, 0)
        return -1 if fnl == sys.maxsize else fnl
