class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        sortedHeights = sorted(heights)
        return sum([1 if sortedHeights[i] != heights[i] else 0 for i in range(len(heights))])
