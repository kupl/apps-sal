class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        b = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                a = (nums[i] - 1) * (nums[j] - 1)
                if b < a and i != j:
                    b = a
        return b
