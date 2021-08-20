class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        res = (nums[0] - 1) * (nums[1] - 1)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if res < (nums[i] - 1) * (nums[j] - 1):
                    res = (nums[i] - 1) * (nums[j] - 1)
        return res
