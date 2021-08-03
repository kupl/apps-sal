class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        called_times = [0] * n
        a = [0] * n
        mod = 10**9 + 7

        for i, j in requests:
            a[j] += 1
            if i - 1 >= 0:
                a[i - 1] -= 1
        c = 0
        for i in range(n - 1, -1, -1):
            c += a[i]
            called_times[i] = c

        called_times.sort(reverse=True)
        nums.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans += called_times[i] * nums[i]
            ans %= mod
            if called_times[i] == 0:
                break
        return ans
