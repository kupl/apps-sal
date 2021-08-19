class Solution:

    def smallestRangeI(self, A: List[int], K: int) -> int:
        (min_element, max_element) = (min(A), max(A))
        return max(0, max_element - min_element - 2 * K)
