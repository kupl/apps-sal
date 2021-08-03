class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maximum_value = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                maximum_value.append((nums[i] - 1) * (nums[j] - 1))
        return max(maximum_value)
