class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        n = [i - 1 for i in nums]
        res = 0
        for (i, j) in itertools.combinations(n, 2):
            res = max(res, i * j)
        return res
