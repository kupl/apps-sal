class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = (10 ** 9 + 7)

        request_counts = [0 for i in range(len(nums))]
        for l, r in requests:
            request_counts[l] += 1
            if r + 1 < len(nums):
                request_counts[r + 1] -= 1
        for i in range(1, len(nums)):
            request_counts[i] += request_counts[i - 1]
        request_counts.sort()
        nums.sort()

        result = 0
        for r, n in zip(request_counts, nums):
            result = (result + r * n) % MOD

        return result
