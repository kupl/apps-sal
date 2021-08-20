class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        max_pro = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = (nums[i] - 1) * (nums[j] - 1)
                if temp > max_pro:
                    max_pro = temp
        return max_pro
