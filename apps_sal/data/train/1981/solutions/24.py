class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        starts = []
        ends = []
        for (x, y) in requests:
            starts.append(x)
            ends.append(y)
        starts.sort()
        ends.sort()
        freqs = [bisect.bisect_right(starts, i) - bisect.bisect_left(ends, i) for i in range(len(nums))]
        freqs.sort()
        nums.sort()
        res = 0
        for (i, j) in zip(freqs, nums):
            res += i * j
        return res % (10 ** 9 + 7)
