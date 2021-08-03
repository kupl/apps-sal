class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n, MOD, ans = len(nums), 10**9 + 7, 0
        count = [0] * (n + 1)
        for s, e in requests:
            count[s] += 1
            count[e + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        have = sorted([c for c in count[:-1] if c], reverse=True)
        nums.sort(reverse=True)
        for a, b in zip(have, nums):
            ans += (a * b) % MOD
            ans %= MOD
        return ans
