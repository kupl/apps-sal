class Solution:

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        i = 0
        end = 0
        res = 0
        while end < T:
            current_end = 0
            while i < len(clips) and clips[i][0] <= end:
                current_end = max(current_end, clips[i][1])
                i += 1
            if current_end <= end:
                return -1
            end = current_end
            res += 1
        return res
