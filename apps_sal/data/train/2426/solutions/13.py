class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        v_min, v_max = min(A), max(A)
        if v_max - v_min >= 2*K:
            return v_max - v_min - 2*K
        else:
            return 0
