class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        a = nums.pop(len(nums) - 1) - 1
        b = nums.pop(len(nums) - 1) - 1
        return a * b
