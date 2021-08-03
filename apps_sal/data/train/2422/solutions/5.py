from itertools import combinations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        comb = list(combinations(nums, 2))
        maxv = 0
        for x in comb:
            if (x[0] - 1) * (x[1] - 1) > maxv:
                maxv = (x[0] - 1) * (x[1] - 1)
        return maxv
