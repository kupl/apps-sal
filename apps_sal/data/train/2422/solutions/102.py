class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for k in range(i + 1, len(nums)):
                if (nums[i] - 1) * (nums[k] - 1) > result:
                    result = (nums[i] - 1) * (nums[k] - 1)
        return result
