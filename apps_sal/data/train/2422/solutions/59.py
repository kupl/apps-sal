import itertools


class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        return max((x * y for (x, y) in itertools.combinations(map(lambda x: x - 1, nums), 2)))
