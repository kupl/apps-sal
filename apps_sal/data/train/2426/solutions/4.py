class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        Max = max(A)
        Min = min(A)
        res = (Max - K) - (Min + K)
        if res < 0:
            return 0
        return res
