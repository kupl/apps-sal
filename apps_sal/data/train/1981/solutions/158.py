class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        import numpy
        weights = numpy.array([0] * len(nums))
        nums = numpy.array(nums)
        for (l, r) in requests:
            weights[l:r + 1] += 1
        nums.sort()
        weights.sort()
        return sum(nums * weights) % (10 ** 9 + 7)
