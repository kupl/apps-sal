class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        print(sorted(nums)[-1] - 1 * sorted(nums)[-2] - 1)
        if len([i for (i, x) in enumerate(nums) if x == max(nums)]) > 1:
            return (max(nums) - 1) ** 2
        else:
            maxi = max(nums)
            other = nums
            nums.remove(maxi)
            return (maxi - 1) * (max(other) - 1)
