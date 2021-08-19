class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort(key=lambda x: [x[0], -x[1]])
        res = 0
        r = 0
        new_r = 0
        # print(clips)
        for s, e in clips:
            if s <= r:
                new_r = max(new_r, e)
            elif s > new_r:
                return -1
            else:
                res += 1
                r = new_r
                # print(new_r)
                new_r = max(new_r, e)
            if new_r >= T:
                break
        if new_r < T:
            return -1
        if r < T and new_r >= T:
            res += 1
        return res
