class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        end, end2, cnt = -1, 0, 0  # end 表示上一段最后截止点，end2表示当前可以最大延伸的最远地点
        for s, e in sorted(clips):
            if end2 >= T or s > end2:  # end2>=T表示已经找到一个可以cover所有T； s>end2表示完全接不上（因为已经排过序了）
                break
            elif end < s <= end2:  # 如果s=end 说明新的这段和上一段有overlap，只需要看新的这段是不是比上一段cover更多 来跟新end2
                cnt += 1
                end = end2
            end2 = max(end2, e)
        return cnt if end2 >= T else -1
