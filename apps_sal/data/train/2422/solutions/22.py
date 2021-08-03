class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        arr = sorted(nums)

        idx1 = nums.index(arr[-1])
        idx2 = nums.index(arr[-2])

        return (nums[idx1] - 1) * (nums[idx2] - 1)
