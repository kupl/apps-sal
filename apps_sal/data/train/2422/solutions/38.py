
from itertools import combinations


class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        combs = list(combinations(nums, 2))
        return max(list([(x[0] - 1) * (x[1] - 1) for x in combs]))
