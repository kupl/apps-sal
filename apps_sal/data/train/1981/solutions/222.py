class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        t = [0] * (n + 1)
        for (a, b) in requests:
            t[a] += 1
            t[b + 1] -= 1
        for i in range(1, n):
            t[i] += t[i - 1]
        nums.sort()
        t.pop()
        t.sort()
        return sum((a * b for (a, b) in zip(nums, t))) % mod
