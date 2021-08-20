class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        dist = max(A) - min(A)
        return dist - 2 * K if dist > 2 * K else 0
