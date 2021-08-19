class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        pref = [0] * n
        for req in requests:
            (l, r) = req
            pref[l] += 1
            if r + 1 < n:
                pref[r + 1] -= 1
        for i in range(1, n):
            pref[i] += pref[i - 1]
        pref.sort()
        nums.sort()
        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            ans = (ans + nums[i] * pref[i]) % MOD
        return ans
