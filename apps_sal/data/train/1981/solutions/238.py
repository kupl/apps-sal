class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        res = 0
        MOD = 10 ** 9 + 7
        ln = len(nums)
        c = [0] * (ln + 1)
        for r in requests:
            c[r[0]] += 1
            c[r[1] + 1] -= 1
        for i in range(1, ln):
            c[i] += c[i - 1]
        nums = sorted(nums, key=lambda x: -x)
        ctr = collections.defaultdict(lambda: 0)
        for cv in c:
            ctr[cv] += 1
        j = 0
        for i in range(len(requests), 0, -1):
            m = ctr[i]
            while m:
                res += nums[j] * i % MOD
                j += 1
                m -= 1
                res = res % MOD
        return res % MOD
