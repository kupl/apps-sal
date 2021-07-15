class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            largest = nums[0]
            second_largest = nums[1]
        else:
            largest = nums[1]
            second_largest = nums[0]
        for i in range(2,len(nums)):
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] > second_largest:
                second_largest = nums[i]
        return (largest-1) * (second_largest -1)
                
                
                

