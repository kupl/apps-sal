class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) >= maxNum and i != j:
                    maxNum = (nums[i] - 1) * (nums[j] - 1)
        return maxNum
