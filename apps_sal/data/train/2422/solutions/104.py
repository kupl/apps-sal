class Solution:

    def maxProduct(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and set(nums) == {1}:
            return 0
        maxi = 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (nums[i] - 1) * (nums[j] - 1) > maxi:
                    maxi = (nums[i] - 1) * (nums[j] - 1)
        return maxi
