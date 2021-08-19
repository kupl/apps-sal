class Solution:

    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        m = len(nums)
        rank = [0] * (m + 1)
        for (i, j) in requests:
            rank[i] += 1
            rank[j + 1] -= 1
        for i in range(1, m):
            rank[i] += rank[i - 1]
        ans = 0
        rank = rank[:m]
        nums.sort()
        rank.sort()
        for (i, count) in enumerate(rank):
            ans += nums[i] * count
        return ans % mod
