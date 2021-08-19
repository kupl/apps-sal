class Solution:

    def isRectangleOverlap(self, r1: List[int], r2: List[int]) -> bool:
        return max(r1[0], r2[0]) < min(r1[2], r2[2]) and max(r1[1], r2[1]) < min(r1[3], r2[3])
