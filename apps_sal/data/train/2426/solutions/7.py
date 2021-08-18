class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        min_val = max_val = A[0]

        for a in A:
            if a < min_val:
                min_val = a
            elif a > max_val:
                max_val = a

        return max(max_val - min_val - 2 * K, 0)
