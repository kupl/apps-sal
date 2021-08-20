class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        ans = 0
        MOD = 10 ** 9 + 7
        N = len(nums)
        walk = Counter()
        for (s, e) in requests:
            walk[s] += 1
            walk[e + 1] -= 1
        vals = []
        amt = 0
        for val in range(0, N):
            amt += walk[val]
            vals.append(amt)
        nums.sort()
        vals.sort()
        ans = 0
        for (v1, v2) in zip(nums, vals):
            ans += v1 * v2
        return ans % MOD
