class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        m = len(requests)
        pre = [0 for i in range(n + 1)]
        for (l, r) in requests:
            pre[l] += 1
            pre[r + 1] -= 1
        cur = 0
        a = [0 for i in range(n)]
        for i in range(n):
            cur += pre[i]
            a[i] = cur
        a.sort()
        nums.sort()
        ans = 0
        for i in range(n):
            ans += nums[i] * a[i]
        return int(ans % (1000000000.0 + 7))
