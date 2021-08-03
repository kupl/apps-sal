class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        return max((max(A) - K) - (min(A) + K), 0)
