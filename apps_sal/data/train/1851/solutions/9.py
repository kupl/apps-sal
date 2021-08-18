class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        end, end2, cnt = -1, 0, 0
        for s, e in sorted(clips):
            if end2 >= T or s > end2:
                break
            elif end < s <= end2:
                cnt += 1
                end = end2
            end2 = max(end2, e)
        return cnt if end2 >= T else -1
