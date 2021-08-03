class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxRes = float('-inf')
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                output = (nums[x] - 1) * (nums[y] - 1)
                if output > maxRes:
                    maxRes = output
        return maxRes
