class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:

        n = len(nums)
        prefix = [0 for i in range(len(nums))]
        for start, end in requests:
            prefix[start] += 1
            if end != n - 1:
                prefix[end + 1] -= 1
        for i in range(1, len(nums)):
            prefix[i] += prefix[i - 1]
        prefix.sort()
        nums.sort()
        res = 0
        mod = 10**9 + 7
        for val, time in zip(prefix, nums):
            res += val * time
        return res % mod
