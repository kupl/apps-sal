class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxNum = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                temp = (nums[i] - 1) * (nums[j] - 1)
                if temp > maxNum:
                    maxNum = temp
        return maxNum
