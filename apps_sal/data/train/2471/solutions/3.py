class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n==0):
            return 0
        if(n<=2):
            return max(nums)
        else:
            dp = [0 for i in nums]
            dp[0] = nums[0]
            dp[1] = nums[1]
            
            for i in range(2,n):
                dp[i] = max(dp[i-1],max(dp[j]+nums[i] for j in range(i-1)))
            return max(dp)

