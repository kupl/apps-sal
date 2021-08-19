class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        (n, MOD) = (len(nums), 10 ** 9 + 7)
        count = [0] * (n + 1)
        for (s, e) in requests:
            count[s] += 1
            count[e + 1] -= 1
        for i in range(1, n):
            count[i] += count[i - 1]
        return sum((a * b for (a, b) in zip(sorted(count[:n]), sorted(nums)))) % MOD
