class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        (a, b) = (max(A), min(A))
        diff = a - b
        coverage = 2 * K
        if diff <= coverage:
            return 0
        else:
            return diff - coverage
