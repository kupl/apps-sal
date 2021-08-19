class Solution:

    def heightChecker(self, heights: List[int]) -> int:
        heights_sort = sorted(heights)
        cnt = 0
        i = 0
        while i < len(heights):
            if heights[i] != heights_sort[i]:
                cnt += 1
            i += 1
        return cnt
