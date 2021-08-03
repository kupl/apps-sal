class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sol = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sol = max(sol, (nums[i] - 1) * (nums[j] - 1))

        return sol
