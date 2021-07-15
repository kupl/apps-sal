class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(nums)-1):
                if nums[i+1]>nums[i]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
                    swapped = True
        return (nums[0]-1)*(nums[1]-1)
