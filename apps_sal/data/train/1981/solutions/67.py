class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = (10**9 + 7)
        n = len(nums)
        count = [0] * (n + 1)
        for i, j in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, n + 1):
            count[i] += count[i - 1]
        ret = 0
        for a, b in zip(sorted(count[:-1]), sorted(nums)):
            ret += a * b
        return ret % MOD
