class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        if (max(A)-min(A)) > K*2:
            return max(A)-min(A) - K*2
        else:
            return 0
