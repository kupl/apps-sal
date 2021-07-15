class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        max_value = max(A) - K
        min_value = min(A) + K
        if max_value > min_value:
            return max_value - min_value
        else:
            return 0
