class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        small, large = 10001, -1
        for x in A:
            small, large = min(x, small), max(x, large)
        return max(large - small - 2 * K, 0)
