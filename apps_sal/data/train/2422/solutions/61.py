class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = 0
        
        nums = [x-1 for x in nums]
        for first in range(len(nums)-1):
            for second in range(first+1, len(nums)):
                prod = nums[first] * nums[second]
                if prod > max_prod:
                    max_prod = prod
        
        return max_prod

