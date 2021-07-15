class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        return A[-1] - A[0] - 2 * K if A[-1] - A[0] > 2 * K else 0
