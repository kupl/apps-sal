class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 if sorted(heights)[i] != heights[i] else 0 for i in range(len(heights))])
