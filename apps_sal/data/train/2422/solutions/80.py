class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        highest = (nums[0] - 1) * (nums[1] - 1)
        c = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                c = (nums[i] - 1) * (nums[j] - 1)
                if c >= highest:
                    highest = c

        return highest
