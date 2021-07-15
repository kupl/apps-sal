class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = float('-inf')
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                ans = max(ans, (nums[i]-1)*(nums[j]-1))
        
        return ans

