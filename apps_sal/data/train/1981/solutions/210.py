class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        rank = [0] * (len(nums) + 1)
        for (i, j) in requests:
            rank[i] += 1
            rank[j + 1] -= 1
        for i in range(1, len(nums)):
            rank[i] = rank[i - 1] + rank[i]
        rank = rank[:-1]
        nums.sort()
        rank.sort()
        total = 0
        for (i, j) in zip(nums, rank):
            total += i * j
        return total % mod
