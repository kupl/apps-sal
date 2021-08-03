class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        dp = [0] * (len(nums) + 1)
        for x, y in requests:
            dp[x] += 1
            dp[y + 1] -= 1

        for i in range(1, len(nums) + 1):
            dp[i] += dp[i - 1]

        res = 0
        for v, c in zip(sorted(dp[:-1]), sorted(nums)):
            res += v * c
        return res % (10**9 + 7)

    # 0,1,2,1,1,0
    # 0 1,0,0,-1,0
    # 1,0,1,0,-1,0
