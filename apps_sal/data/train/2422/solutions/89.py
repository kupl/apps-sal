class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_sum = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                sum = (nums[i] - 1) * (nums[j] - 1)
                if sum > max_sum:
                    max_sum = sum
        return max_sum
