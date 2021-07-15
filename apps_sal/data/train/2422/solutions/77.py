#optimal, one-pass, without sorting

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            max1 = nums[0]
            max2 = nums[1]
        else:
            max1 = nums[1]
            max2 = nums[0]
            
        for i in range(2, len(nums)):
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
            elif nums[i] > max2:
                max2 = nums[i]
                
        return (max1 - 1)*(max2 - 1)
