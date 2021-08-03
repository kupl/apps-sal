class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for idx, num in enumerate(sorted(heights)):
            if heights[idx] != num:
                count += 1

        return count
