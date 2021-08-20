class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        count = [0] * (len(nums) + 1)
        for (i, j) in requests:
            count[i] += 1
            count[j + 1] -= 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        total = 0
        for (a, b) in zip(sorted(count[:-1]), sorted(nums)):
            total += a * b
        return total % (10 ** 9 + 7)
