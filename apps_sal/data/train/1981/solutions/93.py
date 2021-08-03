class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        arr = [0] * n
        for s, e in requests:
            arr[s] += 1
            if e < n - 1:
                arr[e + 1] -= 1
        for i in range(1, n):
            arr[i] += arr[i - 1]
        nums.sort()
        res = 0
        mod = 10**9 + 7
        for a in sorted(arr, reverse=1):
            res += a * nums.pop()
        return res % mod
