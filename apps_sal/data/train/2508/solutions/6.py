class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        heightsSorted = sorted(heights)

        ans = 0
        for i in range(len(heights)):
            if heights[i] != heightsSorted[i]:
                ans += 1

        return ans
