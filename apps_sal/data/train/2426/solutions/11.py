class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        (mx, mn) = (max(A), min(A))
        return max(mx - mn - 2 * K, 0)
