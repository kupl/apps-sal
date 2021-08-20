class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        weights = [0] * n
        for (start, end) in requests:
            weights[start] += 1
            if end + 1 < n:
                weights[end + 1] -= 1
        for i in range(1, n):
            weights[i] += weights[i - 1]
        weights.sort()
        ans = 0
        for (num, weight) in zip(nums, weights):
            ans += num * weight
            ans %= MOD
        return ans
