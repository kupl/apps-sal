class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum = (nums[0] - 1) * (nums[1] - 1)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) > maximum:
                    maximum = (nums[i] - 1) * (nums[j] - 1)
        return maximum
