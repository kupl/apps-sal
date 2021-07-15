class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        dp = [0] * (len(nums)+1)
        
        for r in requests:
            dp[r[0]] += 1
            dp[r[1]+1] -= 1
            
        counts = [0] * len(nums)
        counts[0] = dp[0]
        for i in range(len(nums)):
            counts[i] = counts[i-1] + dp[i]
            
        # print(counts)
        nums.sort()
        counts.sort()
        
        ans = 0
        for n, c in zip(nums, counts):
            ans += n*c
        
        return ans % (10**9+7)
