class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ix = 0
        iy = 0
        ma = 0

        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] * nums[j]) > ma:
                    ma = nums[i] * nums[j]
                    ix = i
                    iy = j

        result = (nums[ix] - 1) * (nums[iy] - 1)

        return result
