class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max = 0
        for x in range(len(nums)):
            for y in range(len(nums)):
                if(y > x):
                    if((nums[x] - 1) * (nums[y] - 1) > max):
                        max = (nums[x] - 1) * (nums[y] - 1)
        return max
