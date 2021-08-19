class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        prod = 0
        for index in range(len(nums) - 1):
            for subindex in range(index + 1, len(nums)):
                cache = (nums[index] - 1) * (nums[subindex] - 1)
                if cache > prod:
                    prod = cache
        return prod
