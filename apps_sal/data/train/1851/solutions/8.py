class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        i = 0
        end = 0
        res = 0

        while end < T:
            current_end = 0
            while i < len(clips) and clips[i][0] <= end:  # basically stating while there is an overlap, keep doing this loop
                current_end = max(current_end, clips[i][1])  # trying to extend end time as far as possible
                i += 1
            if current_end <= end:
                return -1
            end = current_end
            res += 1
        return res  # if the new end is not greater than or equal then it means there are no intervals in which you can extend to the end of the clip
