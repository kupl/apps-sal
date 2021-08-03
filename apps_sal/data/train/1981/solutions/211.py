class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums = sorted(nums, reverse=True)
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        counts = sorted(count, reverse=True)
        res = 0
        for i in range(n):
            res += nums[i] * counts[i]
        return res % (10**9 + 7)
