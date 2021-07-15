class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        max_sums = nums.copy()
        for i, num in enumerate(nums):
            for j in range(0, i - 1):
                if 0 <= j < size:
                    max_sums[i] = max(max_sums[i], num + max_sums[j])
        return max(max_sums)
