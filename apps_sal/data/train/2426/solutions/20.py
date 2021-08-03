class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        mx = max(A)
        mi = min(A)
        return 0 if mx - mi <= 2 * K else mx - mi - 2 * K
