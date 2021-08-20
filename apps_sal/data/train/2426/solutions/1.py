class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        if min(A) + abs(K) > max(A) - abs(K):
            return 0
        else:
            return max(A) - abs(K) - (min(A) + abs(K))
