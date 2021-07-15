class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 **9 + 7
        n = len(nums)
        count = [0] * (n)
        for s, e in requests:
            count[s] += 1
            if e + 1 < n:
                count[e + 1] -= 1
        for i in range(1, n):
            count[i] += count[i-1]
        count.sort()
        nums.sort()
        ans = 0
        for c, a in zip(count, nums):
            ans = (ans + c * a) % MOD
        return ans
