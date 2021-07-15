
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0 # Counter
        b = sorted(heights)
        for x in range(len(heights)):
            if heights[x] != b[x]:
                count += 1
        return count
