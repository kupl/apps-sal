from itertools import combinations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currentMaximum = 0
        for num_i, num_j in combinations(nums, 2):
            if (product := (num_i - 1) * (num_j - 1)) > currentMaximum:
                currentMaximum = product

        return currentMaximum
